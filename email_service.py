#acknowledgement - https://medium.freecodecamp.org/send-emails-using-code-4fcea9df63f
def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

from string import Template

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def email_service():
    names, emails = get_contacts('contacts.txt') # read contacts
    message_template = read_template('messages.txt')

    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login('automatedbabycare@gmail.com','')

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

        # Prints out the message body for our sake
        print(message)

        # setup the parameters of the message
        msg['From']='automatedbabycare@gmail.com'
        msg['To']=email
        msg['Subject']="Your baby is crying"

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # send the message via the server set up earlier.
        s.send_message(msg)

        del msg
    s.quit()
