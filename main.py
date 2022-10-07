import time, random



chips = 1000
winning_numbers_red = [1,3,5,7,9,12,14,16,18,21,23,25,27,28,30,32,34,36]
winning_numbers_black = [2,4,6,8,10,11,13,15,17,19,20,22,24,26,29,31,33,35]
session = True
while session == True:
    roulette_bet_decision = int(input('What you wanna bet on?\t\n1.colors\t\n2.specific numbers\t\n3.Exit '))
    if roulette_bet_decision == 1:
        red_or_black = input("Red or Black (r/b): ")
        if red_or_black == 'r':
            red_chosen = int(input('How much u want to put on red? '))
            if red_chosen <= chips:
                time.sleep(1)
                print(f'You bet {red_chosen} on red.')
                chips - red_chosen
                time.sleep(1)
                roulette_spin_red = random.randint(0,36)
                print('The wheel is spinning...')
                time.sleep(3)
                print(f'The winning number is {roulette_spin_red}')
                if roulette_spin_red in winning_numbers_red:
                    red_chosen * 2
                    chips = chips + red_chosen
                    time.sleep(1.5)
                    print(f'You won {red_chosen} chips!')
                    print(f"Now you have {chips} chips!")
                else:
                    chips = chips - red_chosen
                    time.sleep(1.5)
                    print(f'You lost!')
                    print(f"Now you have {chips} chips!")

            else:
                print('Insufficent funds.. Returning to the beginning...')
                time.sleep(2)
                
        elif red_or_black == 'b':
            black_chosen = int(input('How much u want to put on black? '))
            if black_chosen <= chips:
                time.sleep(1)
                print(f'You bet {black_chosen} on black.')
                chips - black_chosen
                time.sleep(1)
                roulette_spin_black = random.randint(0,36)
                print('The wheel is spinning...')
                time.sleep(3)
                print(f'The winning number is {roulette_spin_black}')
                if roulette_spin_black in winning_numbers_black:
                    black_chosen * 2
                    chips = chips + black_chosen
                    time.sleep(1.5)
                    print(f'You won {black_chosen} chips!')
                    print(f"Now you have {chips} chips!")
                else:
                    chips = chips - black_chosen
                    time.sleep(1.5)
                    print(f'You lost!')
                    print(f"Now you have {chips} chips!")
            else:
                print('Insufficent funds.. Returning to the beginning...')
                time.sleep(2)
        
    elif roulette_bet_decision == 2:
        numbers_betted = []
        betting_ongoing = True
        bet_sum = 0
        while betting_ongoing == True:
            base_bet = int(input('Bet amount/number: '))
            bet_numbers = int(input('What number you want to bet on? (to stop, type "1337")'))
            if bet_numbers < 36:
                numbers_betted.append(bet_numbers)
                time.sleep(1)
                print('Number added!')
                bet_sum = bet_sum + base_bet
            elif bet_numbers > 36 and bet_numbers != 1337:
                print('Type in a number between 0-36')
            elif bet_numbers == 1337:
                betting_ongoing = False
        numbers_betted.sort()
        print(f'Your numbers are {numbers_betted}')
        time.sleep(0.8)
        print('The wheel is spinning...')
        time.sleep(2)
        specific_bet_spin = random.randint(0,36)
        if specific_bet_spin in numbers_betted:
            chips = chips * 36
            print(f'You won! {specific_bet_spin} is the winner number!')
            time.sleep(1)
            print(f'Now you have {chips} chips!')
        else:
            chips = chips - bet_sum
            print('You lost...')
            print(f'Now you have {chips} chips!')
    elif roulette_bet_decision == 3:
        session = False