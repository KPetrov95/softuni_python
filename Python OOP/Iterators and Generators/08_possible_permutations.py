def possible_permutations(ls: list):
    if len(ls) <= 1:
        yield ls
    else:
        for i in range(len(ls)):
            for permutation in possible_permutations(ls[:i] + ls[i + 1:]):
                yield [ls[i]] + permutation

[print(n) for n in possible_permutations([1, 2, 3])]