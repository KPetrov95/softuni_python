total_people = int(input())
wagons = [int(x) for x in input().split()]

for index_wagon in range(len(wagons)):
    people_to_join = min(4 - wagons[index_wagon], total_people)
    total_people -= people_to_join
    wagons[index_wagon] += people_to_join
if total_people > 0:
    print(f"There isn't enough space! {total_people} people in a queue!")
elif any([wagon < 4 for wagon in wagons]):
    print('The lift has empty spots!')
print(*wagons, sep=' ')