from Email import Email
from SMS import SMS


class Message(Email,SMS):
    def __init__(self,emailsend,emailreceiver, emailsubject, smssend, smsreceiver):
        self.message = ''
        self.msgtype = ''
        self.fr0m = ''
        self.to = ''
        self.emailtopic = ''
        Email.__init__(self, semail = emailsend, remail = emailreceiver, subject=emailsubject)
        SMS.__init__(self, sender=smssend, recipient=smsreceiver)
    
    def set_message(self,message):
        self.message = message.capitalize() + ' BYE.'

    def set_msgtype(self):
        while True:
            
            x = input('Type in SMS or Email to choose your message type: ')
            
            if x=='SMS':
                self.msgtype = x
                self.fr0m = self.smssender
                self.to = self.smsreceiver
                break
            
            elif x=='Email':
                self.msgtype = x
                self.fr0m = self.esender
                self.to = self.ereceiver
                self.emailtopic = self.subject
                break
            
            else:
                print('Invalid keyword. Try again.')
    
    def send(self):
  
        print(f"Sending {self.msgtype}...")

        if self.msgtype == 'SMS':

            return 'From: ' + self.fr0m + '\n' + 'To: ' + self.to +  '\n' + self.message
        
        else:

            return 'From: ' + self.fr0m + '\n' + 'To: ' + self.to + '\n' + 'Subject: ' +  '\n' + self.message



m = Message('a1@gmail.com', 'a2@gmail.com', 'Dzień dobry', '789347958', '725737523')

m.set_message('Witam.')

m.set_msgtype()

print(m.send())

