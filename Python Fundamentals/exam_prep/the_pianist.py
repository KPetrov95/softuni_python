def add_piece(pieces, new_piece, new_composer, info):
    if new_piece not in pieces:
        pieces[new_piece] = [new_composer]
        pieces[new_piece].append(info)
        print(f"{new_piece} by {new_composer} in {info} added to the collection!")
    else:
        print(f"{new_piece} is already in the collection!")
    return pieces


def remove_piece(pieces, target_piece):
    if target_piece in pieces:
        pieces.pop(target_piece)
        print(f"Successfully removed {target_piece}!")
    else:
        print(f"Invalid operation! {target_piece} does not exist in the collection.")
    return pieces


def change_key(pieces, changed_piece, new_key):
    if piece_name in pieces:
        pieces[changed_piece][1] = new_key
        print(f"Changed the key of {changed_piece} to {new_key}!")
    else:
        print(f"Invalid operation! {changed_piece} does not exist in the collection.")
    return pieces


number_of_pieces = int(input())

all_pieces = {}
for current_piece in range(number_of_pieces):
    piece, composer, key = input().split('|')
    all_pieces[piece] = [composer, key]


while True:
    command = input().split('|')
    if command[0] == 'Stop':
        break
    if command[0] == 'Add':
        piece_name = command[1]
        piece_composer = command[2]
        piece_key = command[3]
        all_pieces = add_piece(all_pieces, piece_name, piece_composer, piece_key)
    elif command[0] == 'Remove':
        piece_name = command[1]
        all_pieces = remove_piece(all_pieces, piece_name)
    elif command[0] == 'ChangeKey':
        piece_name = command[1]
        key = command[2]
        all_pieces = change_key(all_pieces, piece_name, key)

for key, value in all_pieces.items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")
