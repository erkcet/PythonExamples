from itertools import groupby

text = "aaabbbbcc"
for key, group in groupby(text):
    print(key, len(list(group)))
