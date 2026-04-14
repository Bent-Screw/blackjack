import random
import time
import os

from ascii_cards_main.ascii_cards.cards import kortlek
from ascii_cards_main.ascii_cards.cards import baksida 
random.shuffle(kortlek)


#========================== Print Kort ===========================#


def HorisontellaKort(kortlek):
    # kortlek är den listan med kort som ska skrivas ut


    for kort in range(len(kortlek)):
        
        for tpl in kortlek:

            print_string += str(tpl[kort])
        print_string += '\n'
    print(print_string)


key = ''
bet = 0
sida = 'meny'

while True:

    os.system('cls')

    # hitta saldo
    with open('Blackjack\saldo.txt', 'r') as saldo_fil:
        saldo_val = int(saldo_fil.read().strip())
    
    # time.sleep(1/30)    # kontrollera 'fps' till 30 updateringar i sekunden, ser till att programmet inte käkar prestanda som smågodis

    
    # =============== Visuelt ===================
    if sida == 'meny':

        print('''
        ================ Meny ================
        1. spela
        2. regler




        ''')


        key = input(':  ')

        if key == '1':
            sida = 'spela'

            continue



    if sida == 'spela':
        while True:
            print(f'''
        ================================== Blackjack ==================================
        saldo: {saldo_val} kr
        ''' + '\n' * 5
        )
            
            

            try:
                bet = int(input('bet:   '))
            except ValueError:
                print('skriv input som ett heltal, försök igen')


            
            if saldo_val < bet:
                print('för lite pengar, försök igen')
                time.sleep(1.5)

            elif bet == 0:
                print('du måste satsa mins 1kr')
                time.sleep(1.5)

            else:

                with open('Blackjack\saldo.txt', 'w') as saldo_fil:
                    saldo_fil.write(str(saldo_val - bet))





# ================== Dealer ==================

dealer_kort = []


# ===================== Spelare =====================
spelarkort = []

