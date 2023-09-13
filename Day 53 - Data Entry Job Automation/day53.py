from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time
import requests
import os
from dotenv import load_dotenv

load_dotenv("./.env")

FORM_URL = os.environ.get("FORM_URL")

# --- Extract links, prices and addresses of places to Rent --- #
URL = "https://www.homes.com/manhattan-ny/homes-for-rent/"
headers = {
    "Accept-Language": "en-GB,en;q=0.9,en-US;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76"
}

response = requests.get(url=URL, headers=headers)
data = response.text
soup = BeautifulSoup(data, "html.parser")

divs = soup.find_all('div', class_='for-rent-content-container')

links = []
for div in divs:
    href_value = div.find('a').get('href')
    links.append(f"https://www.homes.com/{href_value}")

prices = []
for div in divs:
    price_value = div.find('a').find('li').get_text().split('p')[0].strip()
    prices.append(price_value)

addresses = []
for div in divs:
    address_p = div.find('a').find('p', class_='address').text
    addresses.append(address_p)

# --- Google Sheets Part --- #
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

for n in range(len(links)):
    driver.get(FORM_URL)
    time.sleep(2)
    input1 = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input1.send_keys(links[n])
    input2 = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input2.send_keys(prices[n])
    input3 = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input3.send_keys(addresses[n])
    submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')
    submit_button.click()