from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
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
        self.driver.get("https://www.instagram.com/433/")
        time.sleep(10)
        followers = self.driver.find_element(By.XPATH, value='//*[@id="mount_0_0_nJ"]/div/div/div[2]/div/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]/button')
        followers.click()
        time.sleep(2)
        modal = self.driver.find_element(By.XPATH, value='/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)
    def follow(self):
        pass

insta = InstaFollower()
# insta.login()

insta.find_followers()