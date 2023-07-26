def add_user(user, side, dictio):
    if side not in dictio.keys():
        dictio[side] = []
    for name in dictio.values():
        if user in name:
            return
    dictio[side].append(user)


def switch_side(user, side, dictio):
    if side not in dictio.keys():
        dictio[side] = []
    for sides, users in dictio.items():
        if user in users:
            dictio[sides].remove(user)
    dictio[side].append(user)
    print(f"{user} joins the {side} side!")


force_statistics = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break
    elif '|' in command:
        force_side, force_user = command.split(' | ')
        add_user(force_user, force_side, force_statistics)

    elif '->' in command:
        force_user, force_side = command.split(' -> ')
        switch_side(force_user, force_side, force_statistics)

for key,value in force_statistics.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        for i in range(len(value)):
            print(f'! {value[i]}')

