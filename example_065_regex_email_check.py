import re

pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
print(bool(re.match(pattern, "user@example.com")))
