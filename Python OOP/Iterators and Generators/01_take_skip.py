class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.start = 0
        self.num_count = 0
    def __iter__(self):
        return self

    def __next__(self):

        num = self.start
        if self.num_count >= self.count:
            raise StopIteration
        self.start += self.step
        self.num_count += 1
        return num

numbers = take_skip(2, 6)
for number in numbers:
    print(number)
