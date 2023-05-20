sheep_pack = input()

sheep_count = 0

pack_list = sheep_pack.split(', ')
if pack_list[-1] == 'wolf':
    print("Please go away and stop eating my sheep")
else:
    for sheep in pack_list[::-1]:
        if pack_list[-1] == 'wolf':
            print(f"Oi! Sheep number {sheep_count}! You are about to be eaten by a wolf!")
            break
        pack_list.pop()
        sheep_count += 1
