from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

for i in range(5):
    add_el_button = driver.find_element(
        By.XPATH, "//button[text()='Add Element']")
    add_el_button.click()

num_del_button = driver.find_elements(
    By.XPATH, "//button[text()='Delete']")
print(len(num_del_button))

sleep(10)

driver.quit()
#Клик по кнопке



