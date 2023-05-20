while True:
    word = input()
    if word == 'End':
        break
    if word == 'SoftUni':
        continue

    for ch in word:
        print(f'{ch}{ch}',end='')

    print()