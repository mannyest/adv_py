

class Counter:
    def __init__(self, low, high, step=1):
        self.current = low
        self.high = high
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):                   # Python 3: def __next__(self)
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += self.step
            return self.current - 1




for c in Counter(3, 8, step=2):
    print(c)


