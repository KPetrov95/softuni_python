import re
dates = input()
pattern = r'\b(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})'
filtered_dates = re.finditer(pattern, dates)
for date in filtered_dates:
    day, month, year = date.group(1), date.group(3), date.group(4)

    print(f'Day: {day}, Month: {month}, Year: {year}')