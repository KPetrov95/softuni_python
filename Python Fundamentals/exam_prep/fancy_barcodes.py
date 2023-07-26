import re

number = int(input())

for i in range(number):
    product_group = '00'
    product = input()
    pattern = r'(@#{1,})([A-Z][A-Za-z0-9]{4,}[A-Z])(@#{1,})'
    valid_product = re.findall(pattern, product)
    if not valid_product:
        print("Invalid barcode")
        continue
    for current_barcode in valid_product:
        product_name = current_barcode[1]
        for current_char in product_name:
            if current_char.isdigit():
                if product_group == '00':
                    product_group = current_char
                else:
                    product_group = product_group + current_char
        print(f"Product group: {product_group}")