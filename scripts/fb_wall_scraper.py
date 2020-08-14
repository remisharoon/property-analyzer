from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.Firefox()
driver.get("https://www.facebook.com/azeem.shahbaz.1")

inputEmail = driver.find_element_by_id("email")
inputEmail.send_keys("fbemail")
inputPass = driver.find_element_by_id("pass")
inputPass.send_keys("fbpass")
inputPass.submit()
page_text = (driver.page_source).encode('utf-8')
soup = BeautifulSoup(page_text)
parse_data = soup.get_text().encode('utf-8').split('Grant Zukel')    
latest_message = parse_data[4]
latest_message = parse_data[4].split('·')
driver.close()
time = latest_message[0]
message = latest_message[1]
print (time,message)