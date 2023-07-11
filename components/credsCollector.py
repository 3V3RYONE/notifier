import os
from dotenv import load_dotenv

class Creds():
    def __init__(self):
        self.username = None
        self.password = None

    def setUsernamePassword(self):
        load_dotenv('../.env')
        
        self.username = os.getenv('username')
        self.password = os.getenv('password')
