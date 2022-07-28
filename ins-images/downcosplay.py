from cmath import log
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import *
import urllib.request

# setup driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.instagram.com/hana.bunny_bunny/")
driver.implicitly_wait(10)

# get email and password from txt
with open('account.txt') as file:
    lines = file.readlines()
    file.close()
account = []
for line in lines:
    line = line.strip()
    account.append(line)
email = account[0]
password = account[1]

# login to instagram
login = driver.find_element(By.CLASS_NAME, "_acas")
login.click()
sleep(2)
name = driver.find_element(By.NAME, "username")
name.clear()
name.send_keys(email)
sleep(2)
password = driver.find_element(By.NAME, "password")
password.clear()
password.send_keys(password)
sleep(2)
login_button = driver.find_element(By.CLASS_NAME, "L3NKy")
login_button.click()
sleep(7)
save_button = driver.find_element(By.CLASS_NAME, "L3NKy")
save_button.click()
sleep(5)

# download images
index = 0
SCROLL_TIMES = 15
for i in range(SCROLL_TIMES):
    images = driver.find_elements(By.CLASS_NAME, "_aagt")
    for img in images:
        index += 1
        src = img.get_attribute('src')
        file_name = f"images/image{index+1000}.png"
        urllib.request.urlretrieve(src, file_name)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(2)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(5)

# close when done downloading images
driver.close()

# keep browser opens
while True:
    pass