size = int(input())

for i in range(size):
    spaces = size - i - 1
    stars = i + 1
    pattern = ' ' * spaces + "* " * stars
    print(pattern)
for i in range(size - 2, -1, -1):
    spaces = size - i - 1
    stars = i + 1
    pattern = ' ' * spaces + "* " * stars
    print(pattern)