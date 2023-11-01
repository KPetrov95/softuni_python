import re

text = input()
pattern = r'>>([A-Za-z]+)<<([0-9]+[\.0-9]*)!([0-9]+)'
total_sum = 0
bought_furniture = []
while text != 'Purchase':
    result = re.search(pattern, text)
    if result:
        furniture, price, quantity = result.groups()
        bought_furniture.append(furniture)
        total_sum += float(price) * int(quantity)
    text = input()
print('Bought furniture:')
for furniture in bought_furniture:
    print(furniture)
print(f'Total money spend: {total_sum:.2f}')