values = [2, 4, 6, 7]
print(any(v % 2 == 1 for v in values))
print(all(v > 0 for v in values))
