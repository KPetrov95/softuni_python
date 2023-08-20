def contains(key, info):
    substring =''.join(info)
    if substring in key:
        print(f"{key} contains {substring}")
    else:
        print("Substring not found!")
    return key


def flip(key, info):
    key_word, start_index, end_index = info
    part_to_change = key[int(start_index): int(end_index)]
    if key_word == "Upper":
        key = key[:int(start_index)] + part_to_change.upper() + key[int(end_index):]
    elif key_word == "Lower":
        key = key[:int(start_index)] + part_to_change.lower() + key[int(end_index):]
    return key


def slice(key, info):
    start_index, end_index = info
    start_index = int(start_index)
    end_index = int(end_index)

    key = key[:start_index] + key[end_index:]
    return key

raw_key = input()

while True:
    command, *data = input().split(">>>")
    if command == 'Generate':
        print(f"Your activation key is: {raw_key}")
        break
    elif command == 'Contains':
        raw_key = contains(raw_key, data)
    elif command == 'Flip':
        raw_key = flip(raw_key, data)
        print(raw_key)
    elif command == 'Slice':
        raw_key = slice(raw_key, data)
        print(raw_key)