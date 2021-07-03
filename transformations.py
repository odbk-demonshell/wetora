#!/usr/bin/env python
import whois # pip install python-whois
from printer import printer
import sys

class transformations:
	def __init__(self):
		self.alert = printer()

	def domainToOrg(self, domain_name):
		try:
			whois_info = whois.whois(domain_name)
			#print(whois_info)
			return whois_info.org
		except:
			print("Unexpected error:", sys.exc_info()[0])
			raise
		return None



# list of registered & non registered domains to test our function
#domains = [
#    "thepythoncode.com",
#    "google.com",
#    "github.com",
#    "unknownrandomdomain.com",
#    "notregistered.co"
#]


# iterate over domains
#for domain in domains:
#    print(domain, "is registered" if is_registered(domain) else "is not registered")