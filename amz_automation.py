from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import time

driver=webdriver.Chrome()
driver.get('https://amazon.in')
time.sleep(2)

searchBox=driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
searchBox.send_keys('mobile')
time.sleep(2)

searchButton=driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input')
searchButton.click()
time.sleep(2)

# getting search bar and search button

review_filter = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[2]/div/div[3]/span/div/div/div/div[2]/ul/span/span/li/span/a/section')
review_filter.click()
time.sleep(2)

# clicking on 4 stars and above filter


slider_min = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[2]/div/div[3]/span/div/div/div/div[5]/div[1]/div[2]/div/form/div[2]/div[1]/div[1]/input")
slider_max = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[2]/div/div[3]/span/div/div/div/div[5]/div[1]/div[2]/div/form/div[2]/div[1]/div[2]/input")

# min and max slider

driver.quit()
# ending the webdriver session

# time.sleep(5000)
