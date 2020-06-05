from flask import render_template, redirect, url_for, flash
from app import app
from app.forms import EmailForm
from app.email import send_email
from app.pitch import Pitch
import os

# time for filling out form: 225.72 seconds

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	return render_template('index.html', title='Sourcing Home')

@app.route('/one_pagers')
def one_pagers():
	return render_template('one_pagers.html', title="One-Pagers")

@app.route('/companies')
def companies():
	return render_template('companies.html', title="Companies")

@app.route('/response')
def response():
	try:
		return render_template('response.html', response=resp[-1])
	except:
		return render_template('response.html', response='No phrase inputted yet')


@app.route('/email_form', methods=['GET', 'POST'])
def email_form():
	form = EmailForm()
	if form.validate_on_submit():
		# include a subject!!!!!
		draft, draft_html = Pitch(form.your_name.data, form.company_name.data, form.contact_person_name.data,
			form.where_find.data, form.impressed_by.data, form.vertical.data).compose_email()
		meta = 'Send final draft to {} at {}\n'.format(form.contact_person_name.data,
			form.contact_person_email.data)
		text_body = meta + draft
		text_html = '<p>'+meta+'<p>'+draft_html
		print(text_body)
		print(text_html)
		send_email('{} Sourcing Email Draft'.format(form.company_name.data),
			sender=app.config['ADMINS'][0],
			recipients=[form.your_email.data], #get from form,
			text_body=text_body,
			html_body=text_html)
		return redirect(url_for('email_sent'))
	return render_template('email_form.html', title='Compose Your Email', form=form)

@app.route('/email_sent')
def email_sent():
	return render_template('email_sent.html')