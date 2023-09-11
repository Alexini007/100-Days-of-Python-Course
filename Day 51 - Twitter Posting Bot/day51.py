from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv("./.env")

PROMISED_DOWNLOAD = 150
PROMISED_UPLOAD = 10
TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
TWITTER_PASS = os.environ.get("TWITTER_PASS")

class InternetSpeedBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        # --- Testing the internet speed --- #
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        accept_button = self.driver.find_element(By.ID, value="onetrust-accept-btn-handler")
        accept_button.click()
        print(accept_button.text)
        time.sleep(3)
        go_button = self.driver.find_element(By.CLASS_NAME, value="start-text")
        print(go_button.text)
        go_button.click()
        time.sleep(60)
        self.up = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        print(self.up)
        self.down = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(self.down)

    def tweet_at_provider(self):
        # --- Login --- #
        self.driver.get("https://twitter.com/login")
        time.sleep(3)
        email = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)
        time.sleep(3)
        time.sleep(3)
        password = self.driver.find_element(By.XPATH, value="//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        password.send_keys(TWITTER_PASS)
        password.send_keys(Keys.ENTER)
        time.sleep(3)

        # --- Write and Publish tweet
        input = self.driver.find_element(By.CSS_SELECTOR, 'br[data-text="true"]')
        input.send_keys(f"Your internet speed is shit, it is only {self.down} download, and {self.up} upload")
        time.sleep(3)
        tweet = self.driver.find_element(By.XPATH, value="//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span")
        tweet.click()
        time.sleep(5)
        print("Tweet Done")
        self.driver.quit()


bot = InternetSpeedBot()
bot.get_internet_speed()
bot.tweet_at_provider()

