import requests
import smtplib
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv("./.env")

my_email = "conkoconkov52@gmail.com"
password = os.environ.get("APP_PASSWORD")
URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
target_price = 100

headers = {
    "Accept-Language": "en-US,en;q=0.9,bg-BG;q=0.8,bg;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

response = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
price = soup.find(class_="a-offscreen").get_text().split("$")[1]
title = soup.find(id="productTitle").get_text().strip()
message = f"{title} is now {price}"
price_float = float(price)
print(price_float)
print(message)

if price_float < target_price:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject: Amazon Price Alert\n\n{message}\n{URL}".encode("utf-8"))
