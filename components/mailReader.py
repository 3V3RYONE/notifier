import imaplib
import email

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
        #import pdb;pdb.set_trace()
        (status, response) = self.mail.search(None, 'UnSeen')
        mail_ids = response[0].split()
        mail_ids = mail_ids[-50:]

        subjects = []

        for itr in mail_ids:
            status, data = self.mail.fetch(itr, '(RFC822)')
            for refined_response in data:
                if type(refined_response) is tuple:
                    plaintxt_msg = email.message_from_bytes((refined_response[1]))
                    if plaintxt_msg['from'] in specified_senders:
                        # Fire whatsapp notification
                        subjects.append(plaintxt_msg['subject'])
                        print(plaintxt_msg['subject'])
                        typ, data = self.mail.store(itr, '+FLAGS', '\\Seen')
        return subjects

