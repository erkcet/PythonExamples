import json

data = {"name": "Ana", "skills": ["python", "sql"]}
text = json.dumps(data)
print(text)
print(json.loads(text)["skills"])
