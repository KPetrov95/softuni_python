budget = int(input())
command = input()
while command != 'End':
    expense = int(command)
    budget -= expense
    if budget < 0:
        print('You went in overdraft!')
        break
    command = input()
if budget >= 0:
    print("You bought everything needed.")
