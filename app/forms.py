from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

# class Form(FlaskForm):
#     input_phrase = StringField('Input a phrase', validators=[DataRequired()])
#     submit = SubmitField('Transmogrify') # hope this id thing works

class EmailForm(FlaskForm):
	# Your name
	# Your email
	# Company name
	# Contact person name
	# Contact person email
	# Where did you find the company
	# impressed by .. .
	# vertical
	
	# Stage 1: everything inputted manually and no memory (+ pretty startup pictures)
	# -----> submit SOMA application
	# Stage 2: input company name and get contact person + email, also get crunchbase 
	# 		   company description and basic background info (like level of funding)
	# 

	# if my next version is built in React, use auto-complete forms to make it easier
	# to find contact info for the company: https://www.digitalocean.com/community/tutorials/react-react-autocomplete


	your_name = StringField('Your Name', validators=[DataRequired()])
	your_email = StringField('Your Email', validators=[DataRequired()])
	company_name = StringField('Company Name', validators=[DataRequired()])
	contact_person_name = StringField('Contact Person Name', validators=[DataRequired()])
	contact_person_email = StringField('Contact Person Email', validators=[DataRequired()])
	where_find = StringField('I found [Company] through...', validators=[DataRequired()])
	impressed_by = StringField('...and was impressed by... ', validators=[DataRequired()])
	vertical = StringField('We also have multiple partners investing in the....', validators=[DataRequired()])
	submit = SubmitField('Send draft to myself')
	# eventually schedule email to be sent from inbox (automatically appy HUCP label)