from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def pageclear():
    i = 0
    while i <= 29:
        print(i)
        if i > 5 and i < 18:
            driver.execute_script("window.scrollTo(0, 700)")
        elif i >= 18:
            driver.execute_script("window.scrollTo(0, 1400)")
        time.sleep(1.5)
        lines = driver.find_elements_by_class_name("td")
        lines[i].click()
        i = i + 1
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='messages_content']/div/form/div[1]/div/a[1]").click()
        time.sleep(2)


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)



driver.get("https://dienynas.tamo.lt/Prisijungimas/Login")



username = driver.find_element_by_id("UserName")
password = driver.find_element_by_id("Password")

Vardas = input("Iveskite savo vartotojo varda: ")
username.send_keys(Vardas)
Slaptazodis = input("Iveskite savo slaptazodi: ")
password.send_keys(Slaptazodis)

password.send_keys(Keys.RETURN)

time.sleep(5)
driver.get("https://dienynas.tamo.lt/Pranesimai")
time.sleep(5)


currentPage = 1
while currentPage <= 5:
    pageclear()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    driver.find_element_by_class_name("forwardPageNumber").click()
    currentPage += 1










