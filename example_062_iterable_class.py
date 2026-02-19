class CountUp:
    def __init__(self, end):
        self.end = end

    def __iter__(self):
        n = 1
        while n <= self.end:
            yield n
            n += 1

print(list(CountUp(4)))
