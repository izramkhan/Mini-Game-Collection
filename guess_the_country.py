import random
import string
import time

import country_data


def animation(message, delay=0.02):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay)

def pick_country_from_world():
    countries = country_data.the_world()
    rand_country = random.choice(countries)
    animation('\nA Random Country Is Selected From The World\n')
    return rand_country

def pick_country_from_specific_continent():
    continent = []

    while True:
        ask_continent = input('\nEnter Continent: ').lower().strip(' ')
        match ask_continent:
            case 'asia':
                continent = country_data.asia()
            case 'europe':
                continent = country_data.europe()
            case 'africa':
                continent = country_data.africa()
            case 'oceania':
                continent = country_data.oceania()
            case 'north america':
                continent = country_data.north_america()
            case 'south america':
                continent = country_data.south_america()
            case 'antartica':
                animation('\n‼️ Can not choose from Antartica!\n')
            case _:
                animation('\n❌ Invalid input! Enter a valid continent')
        
        if continent:
            rand_country = random.choice(continent)
            animation(f'\nA Random Country Is Selected From {ask_continent.title()}\n')
            return rand_country

def world_or_specific_continent():
    while True:
        choose = input('\nEnter 1 -> The World. 2 -> Choose Continent: ')
        if choose == '1':
            rand_country = pick_country_from_world()
            return rand_country
        elif choose == '2':
            rand_country = pick_country_from_specific_continent()
            return rand_country
        animation('\n❌ Enter 1 or 2!\n')

def check_input_validity(guess, err_msg):
    alphabets = string.ascii_letters
    if guess == 'hint':
        return guess
    if guess not in alphabets or len(guess) > 1:
        animation(err_msg)
        return
    return guess

def check_if_lost(lives):
    if lives == 0:
        return lives
    return 
        
def check_if_won(country,):
    if '_' not in country :
        return country
    return

def check_if_word_already_guessed(guess, word_lst, err_msg):
    if guess in word_lst:
        animation(err_msg)
        return 
    return guess

def handle_incorrect_guess(guess, rand_country, lives, word_lst, incrr_word_lst, err_msg):
    if guess not in rand_country:
        word_lst.append(guess)
        incrr_word_lst.append(guess.upper())
        lives -= 1
        animation(err_msg)
        return lives, True
    return lives, False

def handle_correct_guess(guess, rand_country, word_lst, country):
    if guess not in rand_country:
        return
    word_lst.append(guess)
    for index, letter in enumerate(rand_country):
        if guess == letter:
            country[index] = guess
    return guess

def show_country(rand_country, country, incrr_words):
    print('\n----------------------------------------------------------------------')
    for index,(i, j) in enumerate(zip(rand_country, country)):
        if i == '-':
            country[index] = ' '
        print(f'{j.upper()}  ', end='')
    print(f'\n\nWrong guesses: {incrr_words}')
    print('\n----------------------------------------------------------------------')

def get_hint(country, rand_country):
    for index, (i, j) in enumerate(zip(country, rand_country)):
        if i == '_':
            country[index] = j
            return

def intro():
    animation('\n||  *  |  **  GUESS THE COUNTRY  **  |  *  ||\n')
    time.sleep(1)

def ending():
    animation('\n||  *  |  **  ❤️❤️ THANK\'S FOR PLAYING ❤️❤️  **  |  *  ||\n')

def win_celebration():
    animation('\n|--> ❤️🎉 CONGRATES YOU WON THIS ROUND 🎉❤️ <--|')
    time.sleep(1)

def lose_message(rand_country):
    animation(f'\n|--> 💔😑 YOU LOST! THE COUNTRY WAS [{rand_country}] BUT IT\'S OK TRY AGAIN 😙😉 <--|\n')
    time.sleep(1)

def description():
    print('''
          
|----------------------------|
|--    GAME DESCRIPTION    --|
|----------------------------|
          
1. This is a simple command-line game.
2. You can either get a country from the world or from specific continent.
3. HINT: You can have one hint by entering \'hint\' while guessing
4. A random alphabet will pop instead of an underscore to help you out.
5. If you are not able to guess the country in five tries you will lose
6. After each round you will be asked whether you want to play another round or not.
          ''')


def show_round(round):

    animation(f'\nROUND NUMBER: {round}\n')

def guess_the_country():
    random_country = world_or_specific_continent()
    country = ['_'] * len(random_country)
    incorrect_words = []   
    every_word_guessed= []
    lives = 5
    hints = 0
    no_of_guess = 1

    while True:
        show_country(random_country, country, incorrect_words)

        check_lost = check_if_lost(lives)
        if check_lost == 0:
            lose_message(random_country)
            return
        
        check_win = check_if_won(country)
        if check_win == country:
            win_celebration()
            return

        guess = input(f'\nEnter your guess {no_of_guess}: ').lower().strip(' ')

        if guess == 'hint':
            if hints == 0:
                get_hint(country, random_country)
                hints += 1
                continue
            else:
                animation('\nYou have already used your hint!\n')
                continue

        validity = check_input_validity(guess, '\n❌ Enter a single alphabet')
        if not validity:
            continue

        already_guessed = check_if_word_already_guessed(guess, every_word_guessed, '\n‼️ Word already guessed!\n')
        if not already_guessed:
            continue

        lives, was_incorrect = handle_incorrect_guess(guess, random_country, lives, every_word_guessed, incorrect_words, '\n❌ Incorrect guess!\n')
        if was_incorrect:
            no_of_guess += 1
            continue

        was_correct = handle_correct_guess(guess, random_country, every_word_guessed, country)
        if was_correct:
            no_of_guess += 1
            continue

def play_game():

    rounds = 1
    intro()
    description()
    show_round(rounds)
    guess_the_country()

    while True:
        match input('\nWant to play again (y/n): ').lower().strip(' '):
            case 'n':
                ending()
                return
            case 'y':
                rounds += 1
                show_round(rounds)
                guess_the_country()
            case _ :
                animation('\n❌ Enter only (y/n)!')
