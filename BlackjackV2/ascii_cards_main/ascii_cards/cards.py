def print_card(rank, suit):
    '''
    Prints an ASCII representation of a single playing card.

    Args:
        rank (str): The rank of the card ('2'-'10', 'J', 'Q', 'K', 'A').
        suit (str): The suit of the card ('♠', '♥', '♦', '♣').
    '''
    top = '┌─────────┐'
    bottom = '└─────────┘'
    side = '│         │'

    if rank == '10':  # Ten is the only rank with two digits
        rank_right = rank
        rank_left = rank
    else:
        rank_right = rank + ' '
        rank_left = ' ' + rank

    suit_line = f'│    {suit}    │'
    rank_line_left = f'│{rank_left}       │'
    rank_line_right = f'│       {rank_right}│'

    print(top)
    print(rank_line_left)
    print(side)
    print(suit_line)
    print(side)
    print(rank_line_right)
    print(bottom)


def main():
    cards = [('A', '♠'), ('10', '♥'), ('K', '♦'), ('7', '♣')]
    for rank, suit in cards:
        print_card(rank, suit)
        print()  # Add a space between cards






# ================= Redigerat/skapat av Hampus ======================

def append_card(rank, suit):
    '''
    appends an ASCII representation of a single playing card as a list. from top to bottom.

    Args:
        rank (str): The rank of the card ('2'-'10', 'J', 'Q', 'K', 'A').
        suit (str): The suit of the card ('♠', '♥', '♦', '♣').
    '''
    top = '┌─────────┐'
    bottom = '└─────────┘'
    side = '│         │'

    if rank == '10':  # Ten is the only rank with two digits
        rank_right = rank
        rank_left = rank
    else:
        rank_right = rank + ' '
        rank_left = ' ' + rank

    suit_line = f'│    {suit}    │'
    rank_line_left = f'│{rank_left}       │'
    rank_line_right = f'│       {rank_right}│'

    output = []

    output.append(top)
    output.append(rank_line_left)
    output.append(side)
    output.append(suit_line)
    output.append(side)
    output.append(rank_line_right)
    output.append(bottom)

    return output

# hålla koll på mängden av valörer och färger i en kortlek


valörer = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
färger = ['♠', '♥', '♦', '♣']


ascii_kortlek = [] 

for färg in färger:
    for valör in valörer:
        ascii_kortlek.append(tuple(append_card(valör, färg)))


baksida = ('┌─────────┐','│         │','│         │','│ baksida │','│         │','│         │','└─────────┘')



# if __name__ == '__main__':
#     main()
