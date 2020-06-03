from flask import Flask
import os
from flask_mail import Mail
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com' #os.environ.get('MAIL_SERVER')
app.config['MAIL_PORT'] = 587 # int(os.environ.get('MAIL_PORT') or 25)
app.config['MAIL_USE_TLS'] = 1 #os.environ.get('MAIL_USE_TLS') is not None
app.config['MAIL_USERNAME'] = 'hucpsourcer@gmail.com' #os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = 'Love2Source' #os.environ.get('MAIL_PASSWORD')
app.config['ADMINS'] = ['hucpsourcer@gmail.com'] # need to change eventually

mail = Mail(app)
bootstrap = Bootstrap(app)

from app import routes