from collections import defaultdict

text = "hello world"
count = defaultdict(int)
for ch in text.replace(" ", ""):
    count[ch] += 1
print(dict(count))
