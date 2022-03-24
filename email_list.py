####################################################
#   The email_list function receives a dictionary,
# which contains domain names as keys, and a list of
# users as values. Fill in the blanks to generate a
# list that contains complete email addresses
# (e.g. bruce.wayne@gmail.com).
###################################################

def email_list(domains):
	emails = []
	users = []
	for domain in domains.keys():
		users = domains.get(domain, users)
		for user in users:
			email = user + "@" + domain
			emails.append(email)
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker", "tim.cook"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))
