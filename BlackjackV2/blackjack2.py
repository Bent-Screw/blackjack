import random, time
from ascii_cards_main.ascii_cards.cards import ascii_kortlek, baksida

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
            print('Ett sätt att få oändligt med pengar... innan jag tänkte samma sak')
            time.sleep(2.5)

        elif int(bet) <= int(saldo):
            with open('saldo.txt', 'w') as file:
                file.write(f'{int(saldo) - int(bet)}')
            return int(bet)


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
    
    # Återställ saldot till 100 om det är 0 eller mindre
    if saldo <= 0:
        with open('saldo.txt', 'w') as file:
            file.write('100')
        saldo = 100

    if sida == 'meny':
        menu = input('\n'*30 + f'''
        ================== Menu ===================
        saldo: {saldo}kr
        
        1) spela
        2) regler
        3) avsluta programmet
        




        input:  ''')
        print('\n'*20)
        if menu == '1':
            sida = 'bet'
            continue
        elif menu == '2':
            sida = 'regler'

        elif menu == '3':
            print('''
——————Inga Pengar kvar?———————
⠀⣞⢽⢪⢣⢣⢣⢫⡺⡵⣝⡮⣗⢷⢽⢽⢽⣮⡷⡽⣜⣜⢮⢺⣜⢷⢽⢝⡽⣝
⠸⡸⠜⠕⠕⠁⢁⢇⢏⢽⢺⣪⡳⡝⣎⣏⢯⢞⡿⣟⣷⣳⢯⡷⣽⢽⢯⣳⣫⠇
⠀⠀⢀⢀⢄⢬⢪⡪⡎⣆⡈⠚⠜⠕⠇⠗⠝⢕⢯⢫⣞⣯⣿⣻⡽⣏⢗⣗⠏⠀
⠀⠪⡪⡪⣪⢪⢺⢸⢢⢓⢆⢤⢀⠀⠀⠀⠀⠈⢊⢞⡾⣿⡯⣏⢮⠷⠁⠀⠀
⠀⠀⠀⠈⠊⠆⡃⠕⢕⢇⢇⢇⢇⢇⢏⢎⢎⢆⢄⠀⢑⣽⣿⢝⠲⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡿⠂⠠⠀⡇⢇⠕⢈⣀⠀⠁⠡⠣⡣⡫⣂⣿⠯⢪⠰⠂⠀⠀⠀⠀
⠀⠀⠀⠀⡦⡙⡂⢀⢤⢣⠣⡈⣾⡃⠠⠄⠀⡄⢱⣌⣶⢏⢊⠂⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢝⡲⣜⡮⡏⢎⢌⢂⠙⠢⠐⢀⢘⢵⣽⣿⡿⠁⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠨⣺⡺⡕⡕⡱⡑⡆⡕⡅⡕⡜⡼⢽⡻⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣳⣫⣾⣵⣗⡵⡱⡡⢣⢑⢕⢜⢕⡝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣴⣿⣾⣿⣿⣿⡿⡽⡑⢌⠪⡢⡣⣣⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡟⡾⣿⢿⢿⢵⣽⣾⣼⣘⢸⢸⣞⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠁⠇⠡⠩⡫⢿⣝⡻⡮⣒⢽⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
—————————————————————————————''')
            break
        else:
            print('sidan finns inte, försök igen')
            time.sleep(3.5)

    elif sida == 'regler':
            input('Gå till typ wikihow eller nått om du vill veta hur spelet fungerar. skriv vad som helst för att gå till menyn: ')
            sida = 'meny'
            continue


    elif sida == 'bet':
        banner(False)
        print('\n'*8)
        satsning = bet(saldo)
        
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
                time.sleep(3.5)
                sida = 'meny'
                break

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

        continue

    elif sida == 'delarens tur':

        banner(True)
        horisontellaKort(delare_kort)
        print(f'kortvärde:{kort_värde(delare_kort)}')
        print('\n')
        horisontellaKort(spelare_kort)
        print(f'kortvärde:{kort_värde(spelare_kort)}')
        print('\n'*3)



        while True:

            time.sleep(2)
                    # Vinstvillkor    
            # Lägg till nytt kort först (om dealern behöver det)
            if kort_värde(delare_kort) < 17:
                delare_kort.append(kortlek.pop())

            delarvärde = kort_värde(delare_kort)
            prel_delarvärde = kort_värde(delare_kort)
            spelarvärde = kort_värde(spelare_kort)
            
            # Visa korten INNAN vi kollar vinstvillkoren
            banner(True)
            horisontellaKort(delare_kort)
            print(f'kortvärde:{kort_värde(delare_kort)}')
            print('\n')
            horisontellaKort(spelare_kort)
            print(f'kortvärde:{kort_värde(spelare_kort)}')
            print('\n'*3)
            

            
            if delarvärde > 21:
                print('delaren gick över, du vann!')
                with open('saldo.txt', 'w') as file:
                    file.write(str(saldo + satsning*2))
                sida = 'meny'
                time.sleep(3.5)
                break

            elif delarvärde == 21 and delarvärde > spelarvärde:
                print('Delaren fick Blackjack!, du förlorade')
                sida = 'meny'
                time.sleep(3.5)
                break

            elif delarvärde > spelarvärde:
                print('delaren vann, du får hoppas på mer tur nästa gång')
                sida = 'meny'
                time.sleep(3.5)
                break

            elif delarvärde == spelarvärde:
                print('det blev lika, du får pengarna tillbaka')
                sida = 'meny'
                with open('saldo.txt', 'w') as file:
                    file.write(str(saldo + satsning))
                time.sleep(3.5)
                break

            elif delarvärde < spelarvärde: 
                print('du fick högre än delaren, du vann!')
                with open('saldo.txt', 'w') as file:
                    file.write(str(saldo + satsning*2))
                sida = 'meny'
                break

        continue
