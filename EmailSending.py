import smtplib
from email.mime.text import MIMEText
import ssl

"""

A simple program that automates process of sending the same text to multiple emails from one account

Parameters of the function:
1. email_sender - your own email
2. email_password - password of your email
3. email_receivers - list of recipients, who you are aiming to send email to
4. subject - subject of your letter
5. body - text of the letter (in HTML format)

"""
def SendingEmail(email_sender:str,email_password:str, email_receivers:list, subject:str,body:str):
    for email_receiver in email_receivers:
        em = MIMEText(body,'html')
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

