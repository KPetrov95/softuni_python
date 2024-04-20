class vowels:
    vows = "aeiouy"
    def __init__(self, word: str):

        self.word = word
        self.filtered = [x for x in self.word if x.lower() in self.vows]
        self.start_index = 0
        self.end_index = len(self.filtered) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_index > self.end_index:
            raise StopIteration
        index = self.start_index
        self.start_index += 1
        return self.filtered[index]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
