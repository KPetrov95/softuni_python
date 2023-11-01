n = int(input())

car_park = set()

for _ in range(n):
    command, car = input().split(', ')
    if command == 'IN':
        car_park.add(car)
    elif command == 'OUT':
        if car in car_park:
            car_park.remove(car)
if car_park:
    for car in car_park:
        print(car)
else:
    print('Parking Lot is Empty')