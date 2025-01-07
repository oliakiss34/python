from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

for i in range(5):
    addElButton = driver.find_element(By.XPATH, ("//button[text()='Add Element']")).click()

numDelButton = driver.find_elements(By.XPATH, ("//button[text()='Delete']"))
print(len(numDelButton))

sleep(10)
#Клик по кнопке



