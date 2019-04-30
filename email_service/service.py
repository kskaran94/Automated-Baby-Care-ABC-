#acknowledgement - https://medium.freecodecamp.org/send-emails-using-code-4fcea9df63f
from config import email_username, email_password
import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email_service.util import get_contacts, read_template

def email_service():
    names, emails = get_contacts('email_service/contacts.txt') # read contacts
    message_template = read_template('email_service/messages.txt')

    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(email_username,email_password)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

        # Prints out the message body for our sake
        #print(message)

        # setup the parameters of the message
        msg['From']=email_username
        msg['To']=email
        msg['Subject']="Your baby is crying"

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # send the message via the server set up earlier.
        s.send_message(msg)

        del msg
    s.quit()
