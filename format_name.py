####################################################
#   Format name as Last Name, First Name
###################################################

def format_name(first_name, last_name):
	# code goes here
	string =""
	if last_name != "" or first_name != "":
		string ="Name: "
	if last_name != "":
		string = string + last_name
	if last_name != "" and first_name != "":
		string = string + ", "
	if first_name != "":
		string = string + first_name

	return string

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string
