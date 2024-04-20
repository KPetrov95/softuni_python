class countdown_iterator:
    def __init__(self, start_num):
        self.start_num = start_num

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_num < 0:
            raise StopIteration
        num = self.start_num
        self.start_num -= 1
        return num


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
