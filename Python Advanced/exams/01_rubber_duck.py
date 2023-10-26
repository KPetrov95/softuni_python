from collections import deque


time_for_a_task = deque([int(x) for x in input().split()])
number_of_tasks = deque([int(x) for x in input().split()])


ducks_dict = {'Darth Vader Ducky': 0,
              'Thor Ducky': 0,
              'Big Blue Rubber Ducky': 0,
              'Small Yellow Rubber Ducky': 0,
              }
while number_of_tasks and time_for_a_task:
    current_time = time_for_a_task.popleft()
    current_tasks = number_of_tasks.pop()
    time_for_completion = current_time * current_tasks

    if 0 < time_for_completion <= 60:
        ducks_dict['Darth Vader Ducky'] += 1
    elif 61 <= time_for_completion <= 120:
        ducks_dict['Thor Ducky'] += 1
    elif 121 <= time_for_completion <= 180:
        ducks_dict['Big Blue Rubber Ducky'] += 1
    elif 181 <= time_for_completion <= 240:
        ducks_dict['Small Yellow Rubber Ducky'] += 1
    else:
        number_of_tasks.append(current_tasks - 2)
        time_for_a_task.append(current_time)
print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for key,value in ducks_dict.items():
    print(f'{key}: {value}')