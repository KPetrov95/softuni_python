registration = {}
amount = int(input())

for i in range(amount):
    command = input().split()

    if command[0] == 'register':
        name, plate = command[1], command[2]
        if name not in registration:
            registration[name] = plate
            print(f"{name} registered {plate} successfully")
        else:
            print(f'ERROR: already registered with plate number {plate}')
    elif command[0] == 'unregister':
        name = command[1]
        if name not in registration:
            print(f"ERROR: user {name} not found")
        else:
            registration.pop(name)
            print(f"{name} unregistered successfully")

for name, plate in registration.items():
    print(f"{name} => {plate}")