import random
import time

def roll_dice():
    animation('🎲 🔁 🎲 🔁 🎲 🔁 🎲 ...\n')
    return random.randint(1, 6)

def player():
    input('\nPress Enter to roll the dice... ')
    plr_scr = roll_dice()
    return plr_scr

def computer():
    animation('\nComputer is rolling the dice\n')
    computer_score = roll_dice()
    return computer_score

def win_msg():
    animation('\n🎉 Congratulations! You win!')

def lose_msg():
    animation('\n😞 You lose. Better luck next time!')

def tie_msg():
    animation('\nIt\'s a tie! No winner this time!')

def show_what_rolled(plr, comp):
    animation(f'\nYou rolled: {change_to_emoji(plr)} | Computer rolled: {change_to_emoji(comp)}\n')

def show_scores(plr_scr, computer_score):
    print('-' * 40)
    animation(f'Your score: {plr_scr} | Computer score: {computer_score}\n')

def change_to_emoji(any_turn):
    match any_turn:
        case 1:
            any_turn = '1️⃣'
        case 2:
            any_turn = '2️⃣'
        case 3:
            any_turn = '3️⃣'
        case 4:
            any_turn = '4️⃣'
        case 5:
            any_turn = '5️⃣'
        case 6:
            any_turn = '6️⃣'
    return any_turn

def animation(message, delay=0.02):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay)

def description():
    print('''
          
|----------------------------|
|--    GAME DESCRIPTION    --|
|----------------------------|
          
1. Press enter to roll the dice
2. Computer will roll the die
3. First to reach 25 will win the game

- NOTE: If both are above 25 at last turn
      greater score will win!
    
          ''')

def intro():
    animation('\n|| *** | ** WELCOME TO DICE BATTLE ** | *** ||\n')

def play_game():

    intro()
    description()

    plr_scr = 0
    comp_scr = 0

    while True:

        plr_turn = player()
        plr_scr += plr_turn
        
        comp_turn = computer()
        comp_scr += comp_turn

        show_what_rolled(plr_turn, comp_turn)
        show_scores(plr_scr, comp_scr)

        if plr_scr >= 20 and comp_scr < 20:
            win_msg()
            return
        
        elif comp_scr >= 20 and plr_scr < 20:
            lose_msg()
            return
        
        elif plr_scr >= 20 and comp_scr >= 20:
            if plr_scr > comp_scr:
                win_msg()
                return
            elif comp_scr > plr_scr:
                lose_msg()
                return
            else:
                tie_msg()
                return
