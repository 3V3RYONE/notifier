from flask import Flask
from components.credsCollector import Creds
from components.mailReader import AccessEmail

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from notifier!"

@app.route('/read')
def read():
    # initialize creds
    creds = Creds()
    creds.setUsernamePassword()

    # Specify senders
    senders = ['"\'Helpdesk CDC\' via VITIANS CDC Group, Vellore and Chennai Campus" <vitianscdc2024@vitstudent.ac.in>', 'vitianscdc2024@vitstudent.ac.in']

    # read email
    emailReader = AccessEmail(creds.username,
                              creds.password)
    emailReader.logIn()
    mails = emailReader.readUnseen(senders)
    return mails

