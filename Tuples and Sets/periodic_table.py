n = int(input())

chem_elements = set()

for i in range(n):
    elements = input().split()
    for element in elements:
        chem_elements.add(element)

for element in chem_elements:
    print(element)