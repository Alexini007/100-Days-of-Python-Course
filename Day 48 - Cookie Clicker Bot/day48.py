from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")

time_to_check = time.time() + 5
five_min = time.time() + 5*60

playing = True

while playing:
    cookie.click()

    if time.time() > time_to_check: # This will count to see when 5 seconds have passed
        can_buy = []
        items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
        for item in items:
            if item.get_attribute("class") != "grayed":
                can_buy.append(item)

        can_buy[len(can_buy) - 1].click()
        time_to_check = time.time() + 5

    if time.time() > five_min:
        cookie_per_second = driver.find_element(By.ID, value="cps").text
        print(cookie_per_second)
        playing= False

driver.quit()


