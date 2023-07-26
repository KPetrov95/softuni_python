number_of_rooms = int(input())
free_chairs_counter = 0
needed_chairs_flag = False
for room_number in range(number_of_rooms):
    chairs_and_people = input().split(' ')
    chairs = chairs_and_people[0]
    people = int(chairs_and_people[1])
    if len(chairs) >= people:
        free_chairs_counter += len(chairs) - people
    if len(chairs) < people:
        needed_chairs_flag = True
        print(f' {people - len(chairs)} more chairs needed in room {room_number + 1}')

if not needed_chairs_flag:
    print(f"Game On, {free_chairs_counter} free chairs left")