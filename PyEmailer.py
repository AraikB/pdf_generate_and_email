#!/usr/bin/env python3 
import os.path
import mimetypes
import smtplib
import getpass 
from email.message import EmailMessage

#create the object
message = EmailMessage()
#initialize variables to hold email addresses 
sender = "sentazar@gmail.com"  
recipient = "araikb@gmail.com" 
attachment_path = "/tmp/example.png"
attachment_filename = os.path.basename(attachment_path)
mime_type, _ = mimetypes.guess_type(attachment_path) #Guess the mimetype 
mime_type, mime_subtype = mime_type.split('/',1)

#establish header information 
def write_email():
  message['From'] = sender
  message['To'] = recipient 
  message['Subject'] = "Hello {} it's {}!".format(recipient, sender)
  body = '''Hey there {}! I am learning how to write automated emails 
  with python and I thought I would use your email address as a script test" 
  
  Next I'll be sending 1000 messages to test if it works! Make sure to count them!'''.format(recipient)
  message.set_content(body) #sets the body of the message which will be whatever string with 3 ''' the body is set to
  with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
                           maintype=mime_type,
                           subtype = mime_subtype,
                           filename = attachment_filename)


def send_email():
  mail_server = smtplib.SMTP('smtp.mailtrap.io')
  mail_server.set_debuglevel(1)
  mail_pass = getpass.getpass('Password? ') 
  mail_server.login("2692133f26ef96", mail_pass)
  mail_server.send_message(message)
  mail_server.quit()

write_email()
send_email()	


