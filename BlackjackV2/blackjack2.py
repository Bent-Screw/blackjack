import random, time
from ascii_cards_main.ascii_cards.cards import ascii_kortlek, baksida

loop = True

def skapa_kortlek():
    # Spakar ny, blandad kortlek
    kortlek = list(ny_kortlek)
    random.shuffle(kortlek)
    return kortlek

def bet(saldo):
    while True:
        try:
            bet = input('hur mycket vill du satsa?: ')
            int(bet)
        except:
            print('använd bara heltal, försök igen')
            time.sleep(2.5)
            continue

        if int(bet) > int(saldo):
            print('för lite pengar i saldo, försök igen')
            time.sleep(2.5)

        elif int(bet) < 1:
            print('försök inte änns, det fungerar inte')
            time.sleep(2.5)

        elif int(bet) <= int(saldo):
            with open('saldo.txt', 'w') as file:
                file.write(f'{int(saldo) - int(bet)}')
            return bet
            break

def banner(clearTop):

    if clearTop == True:
        print('\n'*20)


    with open('saldo.txt', 'r') as file:
        saldo = int(file.read())
           
    print(f'''
    ============ Blackjack ==============
    saldo: {saldo} kr''')

def horisontellaKort(kort_lista):
    # kort_lista är den listan med kort som ska skrivas ut

    rad = len(kort_lista[0])

    print_string = ''

    # för varje rad
    for rad_idx in range(rad):
        # append första raden för varje kort
        for kort in kort_lista:
            print_string += kort[rad_idx]
        print_string += '\n'

    print(print_string)

def kort_värde(hand):
    värde = 0
    # valörer = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    if not hand:
        return

    rad = len(hand)
    for kort in hand:
        valör = kort[1]

        if '2' in valör:
            värde += 2
        elif '3' in valör:
            värde += 3
        elif '4' in valör:
            värde += 4
        elif '5' in valör:
            värde += 5
        elif '6' in valör:
            värde += 6
        elif '7' in valör:
            värde += 7
        elif '8' in valör:
            värde += 8
        elif '9' in valör:
            värde += 9
        elif '10' in valör:
            värde += 10
        elif 'J' in valör:
            värde += 10
        elif 'Q' in valör:
            värde += 10
        elif 'K' in valör:
            värde += 10
        # just nu så har esset bara värdet 1 istället för att
        # ge valet mellan värde 1 och 10 som i riktiga spelet
        elif 'A' in valör:
            värde += 11
        else:
            värde += 0
            pass

    return värde

# def spelplan(delare_kort, spelare_kort, delarvärde, spelarvärde):
#     banner(True)
#     horisontellaKort(delare_kort)
#     print(f'kortvärde:{kort_värde(delare_kort)}')
#     print('\n')
#     horisontellaKort(spelare_kort)
#     print(f'kortvärde:{kort_värde(spelare_kort)}')
#     print('\n')




saldo = 0
# Läs in saldo från fil eller initiera om det är tomt
try:
    with open('saldo.txt', 'r') as file:
        saldo = int(file.read())
    if saldo <= 0:
        with open('saldo.txt', 'w') as file:
            file.write('100')

except:
    with open('saldo.txt', 'w') as file:
        file.write('100')
        saldo = 100





sida = 'meny'  # Set initial sida as menu
while True:

    with open('saldo.txt', 'r') as file:
        saldo = int(file.read())

    if sida == 'meny':
        menu = input('\n'*30 + f'''
        ================== Menu ===================
        saldo: {saldo}kr
        
        1) spela
        2) regler

        input:  ''')
        if menu == '1':
            sida = 'bet'
            continue
        elif menu == '2':
            sida = 'regler'
        else:
            print('sidan finns inte, försök igen')
            time.sleep(4)

    elif sida == 'regler':
            input('regler är tråkiga, gå till typ wikihow eller nått om du vill veta hur spelet fungerar. skriv vad som helst för att gå till menyn: ')
            sida = 'meny'
            continue
    
    elif sida == 'bet':
        banner(False)
        print('\n'*6)
        bet(saldo)
        
        kortlek = random.sample(ascii_kortlek, len(ascii_kortlek))

        sida = 'dra kort'


    elif sida == 'dra kort':
        
        
        delare_kort = []
        spelare_kort = []

        for i in range(2):
            spelare_kort.append(kortlek.pop())
            delare_kort.append(kortlek.pop())

        prel_delarens_kort = [delare_kort[0], baksida]


        sida = 'spelarens tur'
        loop = True
        pass

    elif sida == 'spelarens tur':
        while True:
            delarvärde = kort_värde(delare_kort)
            prel_delarvärde = kort_värde(prel_delarens_kort)
            spelarvärde = kort_värde(spelare_kort)

            banner(True)
            horisontellaKort(prel_delarens_kort)
            print(f'kortvärde:{kort_värde(prel_delarens_kort)}')
            print('\n')
            horisontellaKort(spelare_kort)
            print(f'kortvärde:{kort_värde(spelare_kort)}')
            print('\n')


            
            if spelarvärde > 21:
                print('Du har gått över, womp womp')
                time.sleep(2)
                break
                sida = 'meny'
                continue

            elif spelarvärde == 21:
                print('Blackjack!')
                sida = 'delarens tur'
                break


            hitPass = input('fortsätt eller stanna (f/s):  ')

            if hitPass == 'f' or hitPass == 'F':
                spelare_kort.append(kortlek.pop())

            elif hitPass == 's' or hitPass == 'S':      
                sida = 'delarens tur'
                break

    elif sida == 'delarens tur':

        banner(True)
        horisontellaKort(delare_kort)
        print(f'kortvärde:{kort_värde(delare_kort)}')
        print('\n')
        horisontellaKort(spelare_kort)
        print(f'kortvärde:{kort_värde(spelare_kort)}')
        print('\n')



        while True:

            time.sleep(1)

            delarvärde = kort_värde(delare_kort)
            prel_delarvärde = kort_värde(delare_kort)
            spelarvärde = kort_värde(spelare_kort)
            
            # Vinstvillkor
            
            if delarvärde > 21:
                print('delaren gick över, du vann!')
                with open('saldo.txt', 'w') as file:
                    file.write(f'{bet*2}')
                sida = 'meny'
                break

            elif delarvärde == 21 and delarvärde > spelarvärde:
                print('Delaren fick Blackjack!, du förlorade')
                sida = 'meny'
                break

            elif delarvärde > spelarvärde:
                print('delaren vann, du får hoppas på mer tur nästa gång')
                sida = 'meny'
                time.sleep(2)
                break

            elif delarvärde == spelarvärde:
                print('det blev lika, du får pengarna tillbaka')
                sida = 'meny'
                time.sleep(2)
                with open('saldo.txt', 'w') as file:
                    file.write(f'{bet}')
                break

            elif delarvärde < spelarvärde: 
                print('du fick högre än delaren, du vann!')
                with open('saldo.txt', 'w') as file:
                    file.write(f'{bet*2}')



            banner(True)
            horisontellaKort(delarens_kort)
            print(f'kortvärde:{kort_värde(_delarens_kort)}')
            print('\n')
            horisontellaKort(spelare_kort)
            print(f'kortvärde:{kort_värde(spelare_kort)}')
            print('\n')
            
            delare_kort.append(kortlek.pop())

            
        # print('weeler dealer')


    elif sida == 'game over':
        # Update the player's balance, display the result, and ask if they want to play again or quit.
        pass

        with open('saldo.txt', 'r') as file:
            saldo = int(file.read())
    
        with open('saldo.txt', 'w') as file:
            file.write('100')