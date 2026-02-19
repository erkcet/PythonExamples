import re

text = "Room 12 costs 45 dollars for 3 nights"
print(re.findall(r"\d+", text))
