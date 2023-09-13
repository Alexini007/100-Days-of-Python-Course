from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

USERNAME = "***"
PASSWORD = "***"


class InstaFollower:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        cookie_accept = self.driver.find_element(By.XPATH, value="/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]")
        cookie_accept.click()
        time.sleep(2)
        email_input = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        email_input.send_keys("***")
        pass_input = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        pass_input.send_keys("***")
        pass_input.send_keys(Keys.ENTER)

    def find_followers(self):
        self.driver.get("https://www.instagram.com/433")
        time.sleep(10)
        followers = self.driver.find_element(By.CSS_SELECTOR, value='//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(2)
        modal = self.driver.find_element(By.XPATH, value='/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value="li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, value='/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


insta = InstaFollower()
insta.login()
insta.find_followers()