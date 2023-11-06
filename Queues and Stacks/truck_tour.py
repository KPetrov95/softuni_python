from collections import deque

number_of_stops = int(input())
sequence_of_stops = deque([int(x) for x in input().split()] for _ in range(number_of_stops))

stops = 0
starting_position = 0

while stops < number_of_stops:
    fuel = 0
    for i in range(number_of_stops):
        fuel += sequence_of_stops[i][0]
        distance = sequence_of_stops[i][1]
        if fuel < distance:
            sequence_of_stops.rotate(-1)
            stops = 0
            starting_position += 1
            break
        fuel -= distance
        stops += 1
print(starting_position)