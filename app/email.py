from flask_mail import Message
from app import *
#from app import mail
import smtplib

def send_email(subject, sender, recipients, text_body, html_body):
	server = smtplib.SMTP()
	server.connect(app.config['MAIL_SERVER'], app.config['MAIL_PORT'])
	msg = Message(subject, sender=sender, recipients=recipients)
	msg.body = text_body
	msg.html = html_body
	mail.send(msg)