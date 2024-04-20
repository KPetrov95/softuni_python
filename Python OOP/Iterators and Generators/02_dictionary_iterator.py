class dictionary_iter:
    def __init__(self, dictio: dict):
        self.dictio = dictio
        self.start = 0
        self.tuples = [(x, y) for x, y in self.dictio.items()]

    def __iter__(self):
        return self

    def __next__(self):

        if self.start > len(self.tuples) - 1:
            raise StopIteration
        item_index = self.start
        self.start += 1
        return self.tuples[item_index]



result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

