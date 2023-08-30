from data_manager import *
from twilio.rest import Client

class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_="+17068072382",
            to="***"
        )
        # Prints if successfully sent.
        print(message.sid)
