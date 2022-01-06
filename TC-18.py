import time

import driver as driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome(executable_path='venv/chromedriver.exe')
driver.get('https://moji.vn/')
driver.set_window_size(1280, 680)
driver.find_element(By.NAME, "q").click()
driver.find_element(By.NAME, "q").send_keys("TÚI")
driver.find_element(By.CSS_SELECTOR, ".head-col-center .fa").click()
articles = driver.find_elements(By.CSS_SELECTOR, 'div.product-item')
for item in articles:
    try:
        title = item.find_element(By.TAG_NAME, 'h3')
        link = item.find_element(By.CSS_SELECTOR, 'h3.name>a')
        print(title.text)
        print(link.get_attribute('href'))
        print('__________')
    except NoSuchElementException:
        pass



time.sleep(2)
driver.quit()