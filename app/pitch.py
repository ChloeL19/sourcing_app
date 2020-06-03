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


	def compose_email(self):
		"""
		Returns a string that will be the message of the sourcing email draft.

		"""
		pass

