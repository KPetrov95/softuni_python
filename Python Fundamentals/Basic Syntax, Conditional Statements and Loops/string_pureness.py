number = int(input())

for i in range(number):
    word = input()
    is_pure = True

    for ch in word:
        if ch == "." or ch == ',' or ch == '_':
            is_pure = False
            print(f"{word} is not pure!")
            break

    else:
        print(f"{word} is pure.")