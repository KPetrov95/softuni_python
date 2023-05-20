n = input()
l = []
for e in str(n):
    l.append(e)
max_num = "".join(sorted(l)[::-1])
print(max_num)
