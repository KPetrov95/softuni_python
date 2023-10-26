def even_odd(*args):
    odd = []
    even = []
    for num in args[:-1]:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    if args[-1] == 'odd':
        return odd

    return even

print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))