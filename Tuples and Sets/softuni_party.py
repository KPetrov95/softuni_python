n = int(input())

list_of_invitations = set()

for i in range(n):
    list_of_invitations.add(input())

while True:
    command = input()
    if command == 'END':
        break
    list_of_invitations.remove(command)

print(len(list_of_invitations))
for no_show in sorted(list_of_invitations):
    print(no_show)