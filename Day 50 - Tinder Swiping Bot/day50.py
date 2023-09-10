from selenium import webdriver
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

# Creating our driver object
tinder_url = "https://tinder.com/app/recs"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(tinder_url)
time.sleep(2)

#-------------------------------AUTHENTICATION----------------------------
accept_button = driver.find_element(By.XPATH, '//*[@id="q-996647900"]/div/div[2]/div/div/div[1]/div[1]/button')
accept_button.click()
time.sleep(2)

log_in_button = driver.find_element(By.XPATH, '//*[@id="q-996647900"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
log_in_button.click()
time.sleep(2)

log_in_with_fb_button = driver.find_element(By.XPATH, '//*[@id="q1569938320"]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
log_in_with_fb_button.click()
time.sleep(5)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]

#------------------------------------------Switching to the Facebook window--------------------------
driver.switch_to.window(fb_login_window)
driver.maximize_window()
time.sleep(2)

accept_cookies_button = driver.find_element(By.CSS_SELECTOR, "._9xo7")
accept_cookies_button.click()
time.sleep(2)

email_entry = driver.find_element(By.ID, "email")
email_entry.send_keys(EMAIL)
time.sleep(1)

password_entry = driver.find_element(By.ID, "pass")
password_entry.send_keys(PASSWORD)
time.sleep(1)

actual_log_in_button = driver.find_element(By.ID, "loginbutton")
actual_log_in_button.click()
time.sleep(2)

#------------------------Switching to the Tinder Window
driver.switch_to.window(base_window)
print(driver.title)
time.sleep(5)

allow_location_button = driver.find_element(By.XPATH, '//*[@id="q1569938320"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()
time.sleep(5)

get_notifications_button = driver.find_element(By.XPATH, '//*[@id="q1569938320"]/div/div/div/div/div[3]/button[1]')
get_notifications_button.click()
time.sleep(5)

dislike_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button')

#---------------------Making 100 swipes----------------------
for n in range(100):

    try:
        time.sleep(2)
        dislike_button.click()

    #--------------------If a popup shows we get rid of it-----------------------
    except ElementClickInterceptedException:
        not_interested_button = driver.find_element(By.XPATH, '//*[@id="q1569938320"]/div/div/div[2]/button[2]')
        not_interested_button.click()

    # try:
    #     print("called")
    #     like_button = driver.find_element(By.XPATH, '//*[@id="q-996647900"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[2]/button')
    #     like_button.click()

    # except ElementClickInterceptedException:
    #     try:
    #         match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
    #         match_popup.click()
    #
    #     except NoSuchElementException:
    #         sleep(2)

print("You have reached your daily limit of swiping!")
driver.quit()