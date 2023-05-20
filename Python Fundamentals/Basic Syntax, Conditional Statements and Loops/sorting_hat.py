voldemort = False
while True:
    name = input()

    if name == "Voldemort":
        voldemort = True
        break
    elif name == 'Welcome!':
        break

    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    else:
        print(f"{name} goes to Hufflepuff.")

if voldemort:
    print("You must not speak of that name!")
else:
    print("Welcome to Hogwarts.")