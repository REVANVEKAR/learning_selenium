from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
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
wait = WebDriverWait(driver, 15)

slider_min = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#p_36\/range-slider_slider-item_lower-bound-slider")))
slider_max = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#p_36\/range-slider_slider-item_upper-bound-slider")))

# min and max slider made it to wait till the buttons are rendered as they are dynamically loaded

driver.execute_script("arguments[0].setAttribute('valuetext', '₹10,000');", slider_min)
driver.execute_script("arguments[0].setAttribute('valuetext', '₹20,000');", slider_max)


go_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[2]/div/div[3]/span/div/div/div/div[5]/div[1]/div[2]/div/form/div[2]/div[2]/span/span/input')
go_button.click()
time.sleep(2)

first_item = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/span/div/div/div/div[2]/div/div/div[1]/h2")
first_item.click()
time.sleep(2)

add_to_cart = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[5]/div[3]/div[1]/div[4]/div/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div/form/div/div/div[37]/div[1]/span/span/span/input")
add_to_cart.click()



driver.quit()
# ending the webdriver session

# time.sleep(5000)
