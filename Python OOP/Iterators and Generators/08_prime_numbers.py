from math import sqrt


def get_primes(ls: list):
    for number in ls:
        if number < 2:
            continue
        for i in range(2, int(sqrt(number)) + 1):
            if number % i == 0:
                break
        else:
            yield number