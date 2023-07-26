initial_deck = input().split()
faro_shuffles_to_be_done = int(input())
for shuffle in range(faro_shuffles_to_be_done):
    middle_of_the_deck = len(initial_deck) // 2
    left_half = initial_deck[0:middle_of_the_deck]
    right_half = initial_deck[middle_of_the_deck:]
    final_deck = []

    for card_index in range(len(left_half)):
        final_deck.append(left_half[card_index])
        final_deck.append(right_half[card_index])
    initial_deck = final_deck

print(initial_deck)
