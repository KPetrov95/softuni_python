def accommodate_new_pets(capacity, max_weight, *args):
    pet_dict = {}
    result = []
    for pet_type, pet_weight in args:
        if capacity <= 0:
            result.append("You did not manage to accommodate all pets!")
            break
        if pet_weight > max_weight:
            continue
        if pet_type not in pet_dict:
            pet_dict[pet_type] = 0
        pet_dict[pet_type] += 1
        capacity -= 1
    else:
        result.append(f"All pets are accommodated! Available capacity: {capacity}.")

    result.append("Accommodated pets:")
    for type_pet, pets_count in sorted(pet_dict.items()):
        result.append(f'{type_pet}: {pets_count}')
    return "\n".join(result)


print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))
