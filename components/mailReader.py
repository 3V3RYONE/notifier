import imaplib
import email
from components.notificationTemplate import Template
from components.notifyWhatsApp import NotifyWhatsApp

class AccessEmail():
    def __init__(self, username, password,
                 imap_url='imap.gmail.com'):
        self.username = username
        self.password = password
        self.imap_url = imap_url
        self.mail = None

    def logIn(self):
        try:
            self.mail = imaplib.IMAP4_SSL(self.imap_url)
            self.mail.login(self.username, self.password)
        except Exception as e:
            raise RuntimeError(e)

    def readUnseen(self, specified_senders):
        self.mail.select('Inbox')
        (status, response) = self.mail.search(None, 'UnSeen')
        mail_ids = response[0].split()
        mail_ids = mail_ids[::-1]
        mail_ids = mail_ids[0:15]

        for itr in mail_ids:
            status, data = self.mail.fetch(itr, '(RFC822)')
            for refined_response in data:
                if type(refined_response) is tuple:
                    plaintxt_msg = email.message_from_bytes((refined_response[1]))
                    if plaintxt_msg['from'] in specified_senders:
                        self.sendWhatsappMessage(plaintxt_msg)
                        typ, data = self.mail.store(itr, '+FLAGS', '\\Seen')

    def sendWhatsappMessage(self, mail):
        body = None
        for part in mail.walk():
            if part.get_content_type() == 'text/plain':
                body = part.get_payload()
        template = Template(mail['from'], mail['subject'], body)
        msg = template.getEmailMessage()
        notification = NotifyWhatsApp(msg)
        notification.accessCreds()
        try:
            notification.sendMessage()
        except Exception as e:
            print('There was a problem while sending the notification to whatsapp: ', e)

