import dice_battle, guess_the_country, guess_the_number, mini_quiz, rock_paper_scissor
import time

def description():
    print('''
          
|--------------------------------------------|
|          -----DESCRIPTION-----             |             
|--------------------------------------------|
          
- Hello and welcome to 'MINI-GAME-COLLLECTION'
          
- There are five games:
- MINI QUIZ
- GUESS THE NUMBER
- GUESS THE COUNTRY
- ROCK PAPER SCISSORS
- DICE BATTLE

- Every game has it own rules that will be told
  at the start of the game   
- Choose a game in the given order

NOTE: Enter '0' to end the program 

          ''')
    time.sleep(1)

def main():
    description()
    while True:
        match input('\nEnter (1 - 5) or 0: ').strip(' '):
            case '0':
                dice_battle.animation('\n ❤️ 🌹 TANKS FOR PLAYING THESE GAME. IT REALLY TOOK AN EFFORT TO CREATE THESE!')
                break

            case '1':
                mini_quiz.mini_quiz()
            case '2':
                guess_the_number.play_game()
            case '3':
                guess_the_country.play_game()
            case '4':
                rock_paper_scissor.play_game()
            case '5':
                dice_battle.play_game()
            case _: 
                dice_battle.animation('\n❌ Error! Enter (1 - 5) or 0 to exit!')
