table = []

for i in range(8):
    table.append([])


def check_winner() -> str | None:
    for c in table:
        if c.count('O') == 3:
            return 'O'
        elif c.count('X') == 3:
            return 'X'

    return None



def add_move(p: str, i: int):
    if i < 0 or i > 7:
        print("Invalid move. Try again.")
        return

    if len(table[i]) >= 3:
        print("Column full. Try again.")
        return

    match i:
        case 0:
            table[0].append(p)
            table[3].append(p)
            table[6].append(p)
        case 1:
            table[0].append(p)
            table[4].append(p)
        case 2:
            table[0].append(p)
            table[5].append(p)
            table[7].append(p)
        case 3:
            table[1].append(p)
            table[3].append(p)
        case 4:
            table[1].append(p)
            table[4].append(p)
            table[6].append(p)
            table[7].append(p)
        case 5:
            table[1].append(p)
            table[5].append(p)
        case 6:
            table[2].append(p)
            table[3].append(p)
            table[7].append(p)
        case 7:
            table[2].append(p)
            table[4].append(p)
            table[5].append(p)
        case _:
            print("Invalid move. Try again.")


while True:
    moves = 0
    turn = 'O'
    u = int(input(f"{turn}'s turn (index of table): "))
    moves += 1

    add_move(turn, u)
    
    if moves != 2:
        winner = check_winner()
        if winner:
            print(f"{winner} wins!")
            break

    if turn == 'O':
        turn = 'X'
    else:
        turn = 'O'