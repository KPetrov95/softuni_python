from _collections import deque

people = deque(input().split())
n = int(input())

counter = 0

while len(people) > 1:
    counter += 1
    current_person = people.popleft()
    if counter == n:
        counter = 0
        print(f"Removed {current_person}")
    else:
        people.append(current_person)
print(f"Last is {people[0]}")