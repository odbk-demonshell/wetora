#!/usr/bin/env python
import whois # pip install python-whois
import sys
import requests
import json
import xml.etree.ElementTree as ET

class transformations:
	def __init__(self):
		self.ripeUrl = "http://rest.db.ripe.net/search?source=ripe&source=lacnic-grs&source=apnic-grs&source=afrinic-grs" \
						"&source=arin-grs&source=jpirr-grs&source=radb-grs&query-string="

	def domainToOrg(self, domain_name):
		try:
			whois_info = whois.whois(domain_name)
			#print(whois_info)
			return whois_info.org
		except:
			print("Unexpected error:", sys.exc_info()[0])
			raise
		return None

	def orgToNameList(self, org_name):
		try:
			response = requests.get(self.ripeUrl+org_name)
			tree = ET.ElementTree(ET.fromstring(response.text))
			namelist = []
			for node in tree.iter():
				if(node.attrib.get("name") == "org-name"):
					namelist.append(node.attrib.get("value"))
			return namelist
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