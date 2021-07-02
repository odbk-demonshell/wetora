#!/usr/bin/env python
import whois # pip install python-whois

class transformations:
	def domainToOrg(self, domain_name):
		whois_info = whois.whois(domain_name)
		print("Organization Name:", whois_info.org)



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