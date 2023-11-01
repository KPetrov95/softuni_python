def validate_ticket(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    ticket_left = ticket[:10]
    ticket_right = ticket[10:]
    winning_symbols = ['@', '#', '$', '^']
    for match_symbol in winning_symbols:
        for uninterrupted_match_length in range(10, 5, -1):
            winning_symbol_repetitions = uninterrupted_match_length * match_symbol
            if winning_symbol_repetitions in ticket_right and winning_symbol_repetitions in ticket_left:
                if uninterrupted_match_length == 10:
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!'
                else:
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}'
    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(', ')]

for ticket in tickets:
    print(validate_ticket(ticket))