def read_next(*args):
    for collection in args:
        for item in collection:
            yield item

for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)

