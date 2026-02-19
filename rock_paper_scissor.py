import random
import time

def animation(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.02)
    time.sleep(0.3)

def ask_rounds():
    while True:
        try:
            rounds = int(input('\nHow many rounds you want to play: '))
            if rounds:
                return rounds
        except ValueError:
            animation('\n❌ Invalid input! Enter a valid number!\n')

def change_to_emoji(any_chc):
    match any_chc:
        case 'r':
            any_chc = '🪨  (rock)'
        case 'p':
            any_chc = '📜  (paper)'
        case 's':
            any_chc = '✂️  (scissor)'
    return any_chc

def show_stats(plr_scr, comp_scr, ties):
    print('-' * 50)
    print(f''' 
Your Score: {plr_scr}
Bot Score:  {comp_scr}
Ties:       {ties}
''')
    print('-'*50)


def show_choice(plr_chc, comp_chc):
    print('\n')
    print('-' * 50)
    animation(f'Your Choice: {change_to_emoji(plr_chc)}\n')
    animation(f'Bot Choice:  {change_to_emoji(comp_chc)}\n')

def show_winner(plr_scr, comp_scr):
    if plr_scr > comp_scr:
        animation('\n🍾🎉  CONGRATULATIONS YOU HAVE WON THE GAME!')
    elif comp_scr > plr_scr:
        animation('\n💔🤖  OH NO! YOU LOST THE ROUND COMPUTER HAS WON THE GAME!')
    else:
        animation('\n🟰  NO ONE WON. YOU BOTH ENDED THE GAME AT SAME SCORE!')

def play_game():

    intro()
    description()

    plr_scr = 0
    comp_scr = 0
    ties = 0
    rounds = ask_rounds()
    round_counter = 1

    while True:

        if rounds == 0:
            show_winner(plr_scr, comp_scr)
            break

        animation(f'\nROUND NUMBER: {round_counter}\n')

        comp_choice = random.choice(['r', 'p', 's'])
        player_choice = input('\nEnter your choice: ').lower().strip(' ')

        if player_choice in ['r', 'p', 's']:

            if player_choice == 'r' and comp_choice == 's':
                plr_scr += 1
            
            elif player_choice == 'p' and comp_choice == 'r':
                plr_scr += 1
            
            elif player_choice == 's' and comp_choice == 'p':
                plr_scr += 1
            
            elif comp_choice == 'r' and player_choice == 's':
                comp_scr += 1
            
            elif comp_choice == 'p' and player_choice == 'r':
                comp_scr += 1
            
            elif comp_choice == 's' and player_choice == 'p':
                comp_scr += 1

            elif comp_choice == player_choice:
                ties += 1
    
            rounds -= 1
            round_counter += 1

            show_choice(player_choice, comp_choice)
            show_stats(plr_scr, comp_scr, ties)

        else:
            animation('\n❌ Invalid input! Enter (r, p, s)!\n')
         
def description():
     print('''
           
|----------------------------|
|--    GAME DESCRIPTION    --|
|----------------------------|

- RULES OF THE GAME:
           
1️⃣  🪨  (rock) beats     -> ✂️  (scissor) 
2️⃣  📜 (paper) beats    -> 🪨  (rock)
3️⃣  ✂️  (scissors) beats -> 📄  (paper)
           
- OPTIONS:
           
r -> Rock 🪨
p -> Paper 📄
s -> Scissors ✂️
    
NOTE: Enter the number of rounds you want to play at the start
''')
     
def intro():
    animation('\n|| *** | ** WELCOME TO ROCK-PAPER-SCISSORS 2.0 ** | *** ||\n')
