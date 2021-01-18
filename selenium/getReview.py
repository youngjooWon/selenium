from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.coupang.com/np/categories/178255")

image = driver.find_elements_by_css_selector(".baby-product-link")[3]
image.click()
time.sleep(3)

reviewTab = driver.find_element_by_name("review")
reviewTab.click()

time.sleep(3)
reviewTxt = driver.find_element_by_css_selector(".sdp-review__highlight__positive__article__content").text
print(reviewTxt)
