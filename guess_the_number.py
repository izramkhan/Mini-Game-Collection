import random
import time

def description():
    print('''
          
|----------------------------|
|--    GAME DESCRIPTION    --|
|----------------------------|
          
Guess the hidden number within the correct range!
You can choose from 5 difficulty levels:
Level 1 (Easy):       1 - 10
Level 2 (Medium):     1 - 100
Level 3 (Hard):       1 - 1,000
Level 4 (Extreme):    1 - 10,000
Level 5 (Impossible): 1 - 100,000
          
- SCORING-SYSTEM 
          
First try          -> 💎 Diamond
Less than 4 tries  -> 🔴 Ruby
Less than 8 tries  -> 🟢 Emerald
Less than 11 tries -> 🟡 Gold
Less than 21 tries -> ⚪ Silver
21 or more tries   -> 🟤 Bronze
          
- NOTE: If your guess is very close (within 5), you will get a hint.
    ''')

close_messages = [
    "\n🔥 Hot! You\'re very close!\n",
    "\n❄️ Cold… but warming up!\n",
    "\n🎯 Almost hit the bullseye!\n",
    "\n👀 You\'re just a few steps away!\n",
    "\n⚡ So close, I can feel the sparks!\n",
]

lvl_1_msg = [
    "\nSo you\'ve chosen the easiest one… afraid of real numbers? 😏\n",
    "\nBaby mode unlocked! 🍼 Let\'s see if you can even handle this.\n",
    "\nNumbers from 1 to 10… wow, such bravery 👏.\n",
]

lvl_2_msg = [
    "\n100 numbers, 1 winner. Will it be you? 🎯\n",
    "\nNot too easy, not too hard… the comfort zone level 🛋️.\n",
    "\nMedium mode… the level for cautious warriors ⚔️.\n",
]

lvl_3_msg = [
    "\nHard mode? Respect 🫡… but don\'t cry later.\n",
    "\nThis is where amateurs break and champions rise 🏆.\n",
    "\nYou really think you can outsmart the odds of 1 in 1000? 🤯\n",
]

lvl_4_msg = [
    "\nThis isn\'t a game anymore, it\'s a war 💣.\n",
    "\nExtreme mode: where hope goes to die 💀.\n",
    "\nYou\'ve chosen madness… may the RNG gods bless you 🙏.\n"
]

lvl_5_msg = [
    "\nIf you win this, I\'ll call you a legend forever 👑.\n",
    "\nImpossible mode: where sanity takes its final breath 🥀.\n",
    "\nYou just unlocked Ultra Madness 🔥… prepare to suffer!\n"
]

def intro():
    animation('\n|| *** | ** WELCOME TO GUESS THE NUMBER 2.0 ** | *** ||\n')
    time.sleep(1)

def animation(message, delay=0.02):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay)

def set_lvl(starting, ending):
    difficulty_range = random.randint(starting, ending)
    return difficulty_range

def ask_lvl():
    rand_num = None
    while True:
        match input('\nChoose a level (1 - 5): '):
            case '1':
                animation(random.choice(lvl_1_msg))
                rand_num = set_lvl(1, 10)
                ending = 10
            case '2':
                animation(random.choice(lvl_2_msg))
                rand_num = set_lvl(1, 100)
                ending = 100
            case '3':
                animation(random.choice(lvl_3_msg))
                rand_num = set_lvl(1, 1000)
                ending = 1000
            case '4':
                animation(random.choice(lvl_4_msg))
                rand_num = set_lvl(1, 10000)
                ending = 10000
            case '5':
                animation(random.choice(lvl_5_msg))
                rand_num = set_lvl(1, 100000)
                ending = 100000
            case _:
                animation('\n❌ Choose between (1-5)!')
                continue
        if rand_num:
            return rand_num, ending

def out_of_range(guess, ending):
    if guess < 1 or guess > ending:
        animation(f'\n‼️Guess out of range! Enter a number in range 1-{ending}\n')
        return True
    return False

def tell_tier(tries, rand_num):
    
    if tries == 1:
        animation(f'\nRIGHT! The number was {rand_num}. You guessed it in first try! TIER: Diamond → 💎\n')

    elif tries <= 3:
        animation(f'\nRIGHT! The number was {rand_num} You guessed it in  {tries} tries. TIER: Ruby → ❤️🔴🟥\n')
        
    elif tries <= 7:
        animation(f'\nRIGHT! The number was {rand_num} You guessed it in {tries} tries. TIER: Emerald → 💚🟢🟩\n')
        
    elif tries <= 10: 
        animation(f'\nRIGHT! The number was {rand_num} You guessed it in {tries} tries. TIER: Gold → 💛🟡🟨\n')
    
    elif tries <= 20:
        animation(f'\nRIGHT! The number was {rand_num} You guessed it in {tries} tries. TIER: Silver → 🩶⬜\n')

    else: 
        animation(f'\nRIGHT! The number was {rand_num} You guessed it in {tries} tries. TIER: Bronze → 🤎🟫\n')

def play_game():

    intro()
    description()

    rand_num, ending = ask_lvl()
    tries = 1

    while True:
        try:
            guess = int(input(f'\nEnter you guess No. {tries}: '))

            if out_of_range(guess, ending):
                continue
            
            elif guess == rand_num:
                tell_tier(tries, rand_num)
                break        

            elif abs(rand_num - guess) <= 5: 
                animation(random.choice(close_messages))
                tries += 1

            elif guess > rand_num:
                animation('\nGuess is higher then the actual number⬆️\n')
                tries += 1

            elif guess < rand_num:
                animation('\nGuess is lower then the actual number⬇️\n')
                tries += 1

        except ValueError:
            animation('\n❌ Invalid input! Enter a valid number!\n')
