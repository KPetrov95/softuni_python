from collections import deque

textiles = deque(int(x) for x in input().split())
meds = deque(int(x) for x in input().split())

items_guide = {30: 'Patch',
               40: 'Bandage',
               100: 'MedKit',
               }
completed_items = {'Patch': 0,
                   'Bandage': 0,
                   'MedKit': 0,
                   }
while textiles and meds:
    current_textile = textiles.popleft()
    current_med = meds.pop()
    sum_items = current_textile + current_med
    if sum_items in items_guide.keys():
        completed_items[items_guide[sum_items]] += 1
    elif sum_items > 100:
        completed_items['MedKit'] += 1
        meds[-1] += sum_items - 100
    else:
        current_med += 10
        meds.append(current_med)

if not textiles and not meds:
    print("Textiles and medicaments are both empty.")
else:
    if not textiles:
        print("Textiles are empty.")
    if not meds:
        print("Medicaments are empty.")
ordered_items = sorted(completed_items.items(), key=lambda kvp: (-kvp[1], kvp[0]))
for item, numbers in ordered_items:
    if numbers > 0:
        print(f'{item} - {numbers}')
if meds:
    print(f"Medicaments left: {', '.join(str(x) for x in reversed(meds))}")
if textiles:
    print(f"Textiles left: {', '.join([str(x) for x in textiles])}")