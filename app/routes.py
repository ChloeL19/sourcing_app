from flask import render_template, redirect, url_for, flash
from app import app
from app.forms import Form, EmailForm
from app.email import send_email
import os

resp = []

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	form = Form()
	if form.validate_on_submit():
		s = Word(form.input_phrase.data)
		resp.append(s.replace())
		return redirect(url_for('response'))
	return render_template('index.html', title='phrase input', form=form)


@app.route('/response')
def response():
	try:
		return render_template('response.html', response=resp[-1])
	except:
		return render_template('response.html', response='No phrase inputted yet')


@app.route('/email_form', methods=['GET', 'POST'])
def email_form():
	form = EmailForm()
	if form.validate_on_submit() and resp:
		print(resp[-1])
		text_body = resp[-1][0] + '\n' + resp[-1][1]
		text_html = '<p>'+resp[-1][0]+'</p>' + '<p>'+resp[-1][1]+'</p>'
		send_email('Your AI-Twisted Phrase',
			sender=app.config['ADMINS'][0],
			recipients=[form.email.data], #get from form,
			text_body=text_body,
			html_body=text_html)
		return redirect(url_for('email_sent'))
	return render_template('email_form.html', title='Email your phrases', form=form)

@app.route('/email_sent')
def email_sent():
	return render_template('email_sent.html')