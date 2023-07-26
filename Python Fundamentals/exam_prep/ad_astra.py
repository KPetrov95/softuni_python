import re

message = input()
pattern = r'([#|])([A-Za-z\s]+\b)\1(\d{2}/\d{2}/\d{2})\1(\d{1,5})\1'

total_calories = 0
items = []
result = re.findall(pattern, message)
if result:
    for match in result:
        nutrition = match[3]
        total_calories += int(nutrition)

days = int(total_calories / 2000)
print(f"You have food to last you for: {days} days!")
if result:
    for match in result:
        current_food = match[1]
        expiration_date = match[2]
        nutrition = match[3]
        total_calories += int(nutrition)
        print(f"Item: {current_food}, Best before: {expiration_date}, Nutrition: {nutrition}")



