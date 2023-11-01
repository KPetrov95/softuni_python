list_of_times = input().split()
finish_line = len(list_of_times) // 2
time_left = 0
time_right = 0
for element in list_of_times[0:finish_line]:
    time = int(element)
    if time == 0:
        if time_left > 0:
            time_left *= 0.8
    time_left += time

for element in list_of_times[-1:finish_line:-1]:
    time_second = int(element)
    if time_second == 0:
        if time_right > 0:
            time_right *= 0.8
    time_right += time_second
if time_right > time_left:
    print(f'The winner is left with total time: {time_left:.1f}')
else:
    print(f'The winner is right with total time: {time_right:.1f}')
