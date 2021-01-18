from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.coupang.com/np/categories/178255")

locate = "dl > dt > img"
images = driver.find_elements_by_css_selector(locate)
count = 1
time.sleep(5)
for image in images:
    try:
        imgURL = image.get_attribute("src")
        print(imgURL)
        urllib.request.urlretrieve(imgURL, "C:\\Users\\YJ\\Desktop\\selenium\\selenium\\img\\" + str(count) + ".jpg")
        count = count + 1       
    except: pass  
driver.close()
