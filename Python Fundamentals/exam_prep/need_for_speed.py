def command_control(dict_of_cars):
    while True:
        command, *data = input().split(" : ")
        if command == 'Stop':
            for key, value in dict_of_cars.items():
                distance, fuel = value
                print(f"{key} -> Mileage: {distance} kms, Fuel in the tank: {fuel} lt.")
            break
        elif command == 'Drive':
            dict_of_cars = drive(dict_of_cars, data)
        elif command == 'Refuel':
            dict_of_cars = refuel(dict_of_cars, data)
        elif command == 'Revert':
            dict_of_cars = revert(dict_of_cars, data)


def drive(dict_of_cars, some_data):
    car, distance, fuel = some_data

    if dict_of_cars[car][1] >= int(fuel):
        dict_of_cars[car][0] += int(distance)
        dict_of_cars[car][1] -= int(fuel)
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
    else:
        print("Not enough fuel to make that ride")
    if dict_of_cars[car][0] >= 100000:
        del dict_of_cars[car]
        print(f"Time to sell the {car}!")
    return dict_of_cars

def refuel(dict_of_cars, some_data):
    car, fuel = some_data
    fuel = int(fuel)
    if dict_of_cars[car][1] + fuel > 75:
        fuel = 75 - dict_of_cars[car][1]
    dict_of_cars[car][1] += fuel
    print(f"{car} refueled with {fuel} liters")
    return dict_of_cars


def revert(dict_of_cars, some_data):
    car, kilometers = some_data
    kilometers = int(kilometers)
    dict_of_cars[car][0] -= kilometers
    if dict_of_cars[car][0] < 10000:
        dict_of_cars[car][0] = 10000
    else:
        print(f"{car} mileage decreased by {kilometers} kilometers")
    return dict_of_cars


number_of_cars = int(input())
garage = {}

for current_car_number in range(number_of_cars):
    car, mileage, fuel = input().split("|")
    garage[car] = [int(mileage), int(fuel)]


command_control(garage)