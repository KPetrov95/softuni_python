import re

text = input()
pattern = r'([=/])([A-Z][a-zA-Z]{2,})\1'
result = re.findall(pattern, text)
travel_points = 0
destinations = []
for current_destination in result:
    valid_destination = current_destination[1]
    destinations.append(valid_destination)
    travel_points += len(valid_destination)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")