def fibonacci():
    prev = 1
    yield 0
    yield 1
    next = 1
    while True:
        i = next
        yield next
        next += prev
        prev = i


generator = fibonacci()
for i in range(10):
    print(next(generator))
