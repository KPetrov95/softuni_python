from collections import deque

MAX_ROTATIONS = 10

seats = input().split(', ')
first_sequence = deque(int(x) for x in input().split(', '))
second_sequence = deque(int(x) for x in input().split(', '))
taken_seats_count = 0
taken_seats = []
rotations = 0

for _ in range(MAX_ROTATIONS):
    rotations += 1
    current_num_one = first_sequence.popleft()
    current_num_two = second_sequence.pop()
    ascii_sign = chr(current_num_one + current_num_two)
    possible_seat_one = str(current_num_one) + ascii_sign
    possible_seat_two = str(current_num_two) + ascii_sign
    if possible_seat_one in seats:
        seats.remove(possible_seat_one)
        taken_seats_count += 1
        taken_seats.append(possible_seat_one)
    elif possible_seat_two in seats:
        seats.remove(possible_seat_two)
        taken_seats_count += 1
        taken_seats.append(possible_seat_two)
    else:
        first_sequence.append(current_num_one)
        second_sequence.appendleft(current_num_two)
    if taken_seats_count == 3:
        break
print(f'Seat matches: {", ".join(taken_seats)}')
print(f'Rotations count: {rotations}')