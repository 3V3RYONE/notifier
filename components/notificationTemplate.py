import os
from dotenv import load_dotenv

class Template():
    def __init__(self, from_, subject, body):
        self.from_ = from_
        self.subject = subject
        self.body = body

    def getEmailMessage(self):
        load_dotenv('../.env')
        name = os.getenv('nameOfTheUser')
        msg = f"{name}, IMPORTANT MAIL is in your inbox!.\n\nFrom: {self.from_}\n\nSubject: {self.subject}\n\nBody: {self.body}"
        return msg
