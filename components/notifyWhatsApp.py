import os
from dotenv import load_dotenv
from twilio.rest import Client

class NotifyWhatsApp():
    def __init__(self, message):
        self.message = message

    def accessCreds(self):
        load_dotenv('../.env')
        self.accountSid = os.getenv('twilioAccountSid')
        self.accountToken = os.getenv('twilioAccountToken')
        self.userPhone = os.getenv('userPhone')
        self.twilioPhone = os.getenv('twilioPhone')
        self.twilioClient = Client(self.accountSid, self.accountToken)

    def sendMessage(self):
        formatFrom = 'whatsapp:' + self.twilioPhone
        formatTo =  'whatsapp:' + self.userPhone
        message = self.twilioClient.messages.create(
                body=self.message,
                from_=formatFrom,
                to=formatTo
                )
