tickets = [n.strip() for n in input().split(", ")]
winning_symbols = ["@", "#", "$", "^"]

for ticket in tickets:

    is_winning = False
    if not len(ticket) == 20:
        print("invalid ticket")

    else:
        left_half = ticket[:10]
        right_halt = ticket[10:]
        for symbol in winning_symbols:
            if ticket.count(symbol) == 20:
                print(f'ticket "{ticket}" - {10}{symbol} Jackpot!')
                is_winning = True
                break

            if (6 * symbol) in left_half and (6 * symbol) in right_halt:
                min_win = min(left_half.count(symbol), right_halt.count(symbol))
                print(f'ticket "{ticket}" - {min_win}{symbol}')
                is_winning = True
                break

        if not is_winning:
            print(f'ticket "{ticket}" - no match')
