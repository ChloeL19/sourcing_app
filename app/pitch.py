# import stuff

import requests 
import json

# create a Word class (phrase)
class Pitch:

	def __init__(self, your_name, company_name, contact_person_name, where_find, impressed_by,
		vertical):
		self.your_name = your_name
		self.company_name = company_name
		self.contact_person_name = contact_person_name
		self.where_find = where_find
		self.impressed_by = impressed_by
		self.vertical = vertical

	def first_name(self, name):
		return name.split(" ")[0]

	def compose_email(self):
		"""
		Returns a string that will be the message of the sourcing email draft.

		"""
		msg = "Hi {}, \n\
		I hope this finds you well. I’m {}, a member of the Harvard Capital Partners (HUCP),\
		an undergraduate club that connects promising start-ups with our ~40 angel and VC partners\
		who invest in early-stage start-ups.\n \
		I found {} through the Harvard Innovation Labs and was impressed by how you’re \
		{}. We also have multiple\
		partners investing in the {} that may be interested. If you're interested, I’d enjoy video\
		chatting briefly when convenient to share more about HUCP’s investing partners and learn more about\
		 {}.\n\
		Hope to talk with you soon.\n \
		Best,\n\
		{}".format(self.contact_person_name, self.your_name, self.company_name, self.where_find, self.vertical, 
			self.company_name, self.your_name)

		msg_test = "Hi {},\
		I hope this finds you well. I’m {}, a member of the Harvard Capital Partners (HUCP),\
		an undergraduate club that connects promising start-ups with our ~40 angel and VC partners\
		who invest in early-stage start-ups.\
		I found {} through the Harvard Innovation Labs and was impressed by how you’re \
		{}. We also have multiple\
		partners investing in the {} that may be interested. If you're interested, I’d enjoy video\
		chatting briefly when convenient to share more about HUCP’s investing partners and learn more about\
		 {}.\
		Hope to talk with you soon. \
		Best,\
		{}".format(self.contact_person_name, self.your_name, self.company_name, self.where_find, self.vertical, 
			self.company_name, self.your_name)


		msg_html = "<p>Hi {}, </p>\
		<p>I hope this finds you well. I’m {}, a member of Harvard Undergraduate Capital Partners (HUCP),\
		an undergraduate club that connects promising start-ups with our ~40 angel and VC partners\
		who invest in early-stage start-ups.</p> \
		<p>I found {} through {} and was impressed by how you’re \
		{}. We also have multiple\
		partners investing in the {} that may be interested.</p> <p>If you're interested, I’d enjoy video\
		chatting briefly when convenient to share more about HUCP’s investing partners and learn more about\
		 {}.</p>\
		<p>Hope to talk with you soon.</p> \
		<p>Best,</p>\
		<p>{}</p>".format(self.first_name(self.contact_person_name), self.first_name(self.your_name), self.company_name, 
			self.where_find, self.impressed_by,
			self.vertical, self.company_name, self.first_name(self.your_name))

		return msg_test, msg_html


