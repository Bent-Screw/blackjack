import random
import time
import os
import keyboard

from ascii_cards_main.ascii_cards.cards import kortlek
# from ascii_cards_main.ascii_cards.cards import baksida 
# orkade inte få det att fungera med import
baksida = ['┌─────────┐','│         │','│         │','│         │','│         │','│         │','└─────────┘']



#========================== Print Kort ===========================#


def HorisontellaKort(kort_lista):
    # kort_lista är den listan med kort som ska skrivas ut
    
    # om funktionen används utan input så returneras det utan att krasha
    if not kort_lista:
        return
    
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
            pass

    return värde


def återställ():
    global sida, hit, bet_satt
    time.sleep(3)
    print('\n'*10)
    sida = 'meny'
    hit = False
    bet_satt = False


key = ''
bet = 0
sida = 'meny'
bet_satt = False

# ordning
delakort = False



while True:

    #os.system('cls')

    # hitta saldo
    with open('saldo.txt', 'r') as saldo_fil:
        saldo_val = int(saldo_fil.read().strip())

    if saldo_val < 1:
        print('du har slut med pengar, men du får en chans till. Ditt saldo har återställts till 100 kr.')
        with open('saldo.txt', 'w') as saldo_fil_w:
            saldo_fil_w.write('100')

    if sida == 'meny':

        print('''
        ================ Meny ================
        1. spela
        2. regler




        ''')


        key = input(':  ')

        if key == '1':
            sida = 'spela'
            key = ''




    if sida == 'spela':
        
        while bet_satt == False:

            # hitta saldo
            with open('saldo.txt', 'r') as saldo_fil:
                saldo_val = int(saldo_fil.read().strip())

            os.system('cls')

            print(f'''
        ================================== Blackjack ==================================
        saldo: {saldo_val} kr
        ''' + '\n' * 2
        )
            
            # satsa 
            try:
                bet = int(input('bet:   '))
            except ValueError:
                print('skriv input som ett heltal, försök igen')

            if saldo_val < bet:
                print('du har för lite pengar i ditt saldo, försök igen')
                time.sleep(1.5)

            elif bet == 0:
                print('du måste satsa minst 1kr')
                time.sleep(1.5)

            else:

                with open('saldo.txt', 'w') as saldo_fil:

                    saldo_fil.write(str(saldo_val - bet))
                
                bet_satt = True
                gambling = True
                

                #====== Gör en blandad koppia av kortleken ======
                spelkortlek = kortlek  # skapa kopia

                random.shuffle(spelkortlek)   # blanda  
        



                # ge första korten till dealer 

                dealer_kort = []
                for i in range(1):
                    dealer_kort.append(spelkortlek.pop(0))
                

                dealer_kort_visas = []
                dealer_kort_visas.append(dealer_kort[0])
                dealer_kort_visas.append(baksida)

                # ge första korten till spelare  

                spelarens_kort = []
                for i in range(2):
                    spelarens_kort.append(spelkortlek.pop(0))

            hit = True

            # ========= gambling ==========




        while hit == True:




                    # hitta saldo, igen
            with open('saldo.txt', 'r') as saldo_fil:
                saldo_val = int(saldo_fil.read().strip())

                print(f'''
        ================================== Blackjack ==================================
        saldo: {saldo_val} kr
        ''' + '\n' * 2
        )
            HorisontellaKort(dealer_kort_visas)
            print(f'värdet på korten: {kort_värde(dealer_kort)}')

            print('\n' * 3)

            HorisontellaKort(spelarens_kort)
            print(f'värdet på korten: {kort_värde(spelarens_kort)}')




            hit_pass = input('fortsätt eller stanna (f/s):   ')

            if hit_pass == 'f' or hit_pass == 'F':
                spelarens_kort.append(spelkortlek.pop(0))
                print('\n' * 2)
                HorisontellaKort(spelarens_kort)
                print(f'värdet på korten: {kort_värde(spelarens_kort)}')

            elif hit_pass == 's' or hit_pass == 'S':
                print('pass')
                dealer_kort_visas = dealer_kort[:]
                hit = False
                
                # Dealern drar kort tills värdet är 17 eller högre
                while kort_värde(dealer_kort) < 17:
                    time.sleep(0.5)
                    dealer_kort.append(spelkortlek.pop(0))
                    dealer_kort_visas = dealer_kort[:]
                    print('\n' * 2)
                    HorisontellaKort(dealer_kort_visas)
                    print(f'värdet på korten: {kort_värde(dealer_kort)}')
                
                break



            # över eller under 21?
            if kort_värde(spelarens_kort) > 21:
                print('Dina kort har värde över 21, du förlorade')
                återställ()

            elif kort_värde(spelarens_kort) == 21:
                print('Blackjack! du vinner')
                with open('saldo.txt', 'w') as saldo_fil:
                    saldo_fil.write(str(int(saldo_val + bet*2.5)))
                återställ()

            elif kort_värde(dealer_kort) == kort_värde(spelarens_kort):
                print('oavgjort, du får tillbaka dina pengar')
                with open('saldo.txt', 'w') as saldo_fil:
                    saldo_fil.write(str(saldo_val + bet))
                återställ()
                
            elif kort_värde(dealer_kort) > 21:
                print('Delaren har gått över 21, du vinner')
                with open('saldo.txt', 'w') as saldo_fil:
                    saldo_fil.write(str(saldo_val + bet * 2))
                återställ()
                
            elif kort_värde(dealer_kort) == 21:
                print('Delaren fick Blackjack! du förlorade')
                återställ()

            elif kort_värde(dealer_kort) > kort_värde(spelarens_kort) and kort_värde(dealer_kort) < 22:
                print('delaren fick högst, du förlorar')
                återställ()
