from collections import Counter

words = "to be or not to be".split()
print(Counter(words).most_common(2))
