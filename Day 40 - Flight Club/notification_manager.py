from data_manager import *
from twilio.rest import Client
import smtplib
import os
from dotenv import load_dotenv

load_dotenv("./.env")
my_email = "conkoconkov52@gmail.com"
password = os.environ.get("APP_PASSWORD")
class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)


    def send_emails(self, emails, message):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(my_email, password)
            for email in emails:
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
