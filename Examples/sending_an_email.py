#!/usr/bin/python3

import smtplib

sender = 'lovelydove941@gmail.com' # input('Sender: ')
reciver = 'caninetable@gmail.com' # input('reciver: ')
password = 'sS332722560' # input('Password: ')
subject = 'python smtplib lib' # input('Subject: ')
body = 'if you have recived this email, then the python bot was successful.' # input('Body: ')

message = f"""From: Python {sender}
To: {reciver}
Subject: {subject}
{body}
"""
try:
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()

    server.login(sender,password)
    print('Logged in')
    server.sendmail(sender, reciver, message)
    print('email has been sent')

except smtplib.SMTPAuthenticationError:
    print('unable to sign in.')