from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# launch browser
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument('--log-level=3')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver.get("https://www.leagueofgraphs.com")
driver.get("https://www.leagueofgraphs.com/tft/champions")
driver.implicitly_wait(5)

# interact browser
def getOneChampMain(champ):
    search = driver.find_element('xpath', "/html/body/div[2]/div[3]/div[2]/div[1]/div/form/input")
    search.send_keys(str(champ))
    search.send_keys(Keys.RETURN)
    button = driver.find_element('xpath', "/html/body/div[2]/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[5]/table/tbody/tr[12]/td/a/button")
    button.click()
    try:
        table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div[3]/div[2]/div[2]/div[1]/div/div/table"))
        )
    except:
        driver.quit()
    names = table.find_elements(By.CLASS_NAME, 'name')
    res = []
    i = 1
    for name in names:
        res.append(f'Top {i}: {name.text}')
        i += 1
    return res

def delayedElement(by, path):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((by, path))
        )
    except:
        driver.quit()
    return element

def getChampInfo():
    # ability_image = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[3]/div[2]/div[2]/div/div[1]/div[2]/div[1]").find_element(By.TAG_NAME, "img").get_attribute("src")                                                                                                                                      
    ability_desc = driver.find_element(By.CLASS_NAME, "abilityDescription").text
    tier = driver.find_element(By.CLASS_NAME, "solo-number").text
    champ_class = driver.find_element(By.CLASS_NAME, "bannerSubtitle").text
    # champ_image = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[1]/div/div[1]/div/img").get_attribute('src')
    champ = driver.find_element(By.CLASS_NAME, "pageBanner").find_element(By.TAG_NAME, 'h2').text
    return {
        'name': champ,
        'class': champ_class,
        'tier': tier,
        'description': ability_desc
    }

table = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[3]/div[2]/div[2]/div/div/div/table")
champs = table.find_elements(By.CLASS_NAME, 'name')
champ_data = []
for champ in champs:
    champ.click()
    champ_data.append(getChampInfo())
    driver.back()

with open("tftdata.txt", "w") as file:
    file.write(str(champ_data))
    file.close()

while(True):
    pass