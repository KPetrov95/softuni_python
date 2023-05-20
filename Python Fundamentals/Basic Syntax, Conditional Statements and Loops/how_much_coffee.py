coffees = 0
activity_list = ["coding", "dog", "cat", "movie", 'CODING', 'DOG', 'CAT', 'MOVIE']

while True:
    command = input()
    if command == 'END':
        break
    if command in activity_list:
        if command.isupper():
            coffees += 2
        else:
            coffees += 1

if coffees <= 5:
    print(coffees)
else:
    print("You need extra sleep")
