class sequence_repeat:
    def __init__(self, sequence: str, num: int):
        self.sequence = sequence
        self.num = num
        self.start = 0
        self.start_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.num:
            raise StopIteration
        current_index = self.start_index
        self.start_index += 1
        self.start += 1
        if self.start_index >= len(self.sequence):
            self.start_index = 0
        return self.sequence[current_index]

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')

