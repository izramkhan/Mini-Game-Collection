import time

easy_qst = [
    # Math
    ['What is 12 + 15?', '25', '26', '27', '28', 'C'],
    ['What is 9 × 9?', '72', '81', '99', '90', 'B'],

    # Physics
    ['What is the unit of force?', 'Joule', 'Newton', 'Watt', 'Pascal', 'B'],
    ['What planet do we live on?', 'Mars', 'Venus', 'Earth', 'Jupiter', 'C'],

    # Computer Science
    ['Which device is used to input text?', 'Monitor', 'Keyboard', 'Printer', 'Speaker', 'B'],
    ['Which number system uses only 0 and 1?', 'Decimal', 'Binary', 'Octal', 'Hexadecimal', 'B'],

    # History
    ['Who was the first President of the United States?', 'Lincoln', 'Washington', 'Jefferson', 'Adams', 'B'],
    ['In which year did World War II end?', '1945', '1939', '1918', '1950', 'A'],

    # General Knowledge
    ['What is the largest ocean?', 'Indian', 'Atlantic', 'Pacific', 'Arctic', 'C'],
    ['How many days are in a leap year?', '364', '365', '366', '367', 'C']
]

med_qst = [
    # Math
    ['What is the derivative of 3x?', '3', 'x', '3x', '0', 'A'],
    ['What is the value of π (approx)?', '2.14', '3.14', '4.13', '3.41', 'B'],

    # Physics
    ['What is acceleration due to gravity on Earth?', '9.8 m/s^2', '8.9 m/s^2', '10.5 m/s^2', '7.8 m/s^2', 'A'],
    ['What phenomenon bends light in water?', 'Reflection', 'Refraction', 'Diffusion', 'Radiation', 'B'],

    # Computer Science
    ['What is the time complexity of linear search?', 'O(1)', 'O(n)', 'O(log n)', 'O(n^2)', 'B'],
    ['Which data structure follows FIFO?', 'Stack', 'Queue', 'Tree', 'Graph', 'B'],

    # History
    ['Who unified Germany in 1871?', 'Napoleon', 'Bismarck', 'Hitler', 'Churchill', 'B'],
    ['The Ottoman Empire collapsed after which war?', 'WWI', 'WWII', 'Cold War', 'Crimean War', 'A'],

    # General Knowledge
    ['What is the capital of Australia?', 'Sydney', 'Melbourne', 'Canberra', 'Perth', 'C'],
    ['Which element has the symbol Na?', 'Nitrogen', 'Neon', 'Sodium', 'Nickel', 'C']
]

hard_qst = [
    # Math
    ['What is the integral of 2x dx?', 'x^2 + C', '2x + C', 'x + C', '2 + C', 'A'],
    ['If matrix [[1,2],[3,4]], what is its determinant?', '-2', '2', '-1', '1', 'A'],

    # Physics
    ['Which theory predicts time dilation?', 'Quantum Mechanics', 'Special Relativity', 'Thermodynamics', 'Classical Mechanics', 'B'],
    ['What is the SI unit of electric charge?', 'Volt', 'Ampere', 'Coulomb', 'Ohm', 'C'],

    # Computer Science
    ['What is the average time complexity of merge sort?', 'O(n)', 'O(log n)', 'O(n log n)', 'O(n^2)', 'C'],
    ['What is the time complexity of inserting into a binary heap?', 'O(1)', 'O(log n)', 'O(n)', 'O(n log n)', 'B'],

    # History
    ['The Peace of Westphalia (1648) established what principle?', 'Democracy', 'Colonialism', 'National Sovereignty', 'Communism', 'C'],
    ['Which treaty ended World War I?', 'Treaty of Paris', 'Treaty of Versailles', 'Treaty of Rome', 'Treaty of Vienna', 'B'],

    # General Knowledge
    ['Which country has the most natural lakes?', 'USA', 'Russia', 'Canada', 'Brazil', 'C'],
    ['What supercontinent existed before Pangaea?', 'Gondwana', 'Laurasia', 'Rodinia', 'Baltica', 'C']
]

def animation(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    time.sleep(0.5)

def ask_difficulty():
    qst_lst = None
    difficulty = None
    while True:
        match input('\nEnter difficulty level (1/2/3): '):
            case '1':
                qst_lst = easy_qst
                difficulty = 'easy 🟢'
            case '2':
                qst_lst = med_qst
                difficulty = 'medium 🟨'
            case '3':
                qst_lst = hard_qst
                difficulty = 'hard 🟥'
            case _:
                animation('\n❌ Invalid Input! Enter (1/2/3)!\n')
            
        if qst_lst:
            animation(f'\nCHOOSEN DIFFICULTY LEVEL: {difficulty.upper()}')
            return qst_lst
        
def set_price(qst_lst):
    prz_per_qst = 0
    if qst_lst == easy_qst:
        prz_per_qst = 100
    elif qst_lst == med_qst:
        prz_per_qst = 200
    elif qst_lst == hard_qst:
        prz_per_qst = 300

    return prz_per_qst

def mini_quiz():

    intro()
    description()

    crr_ans = 0
    qst_lst = ask_difficulty()
    prz_per_qst = set_price(qst_lst)
    
    for qst_no, question in enumerate(qst_lst, start=1):
        print('\n')
        print('-'*60)
        print(f'Q{qst_no} ➤ {question[0]}')
        print('-'*60)
        print(f'(A) {question[1]}     (B) {question[2]}')
        print(f'(C) {question[3]}     (D) {question[4]}')
        print('-'*60)

        while True:
            ans = input('\nEnter your answer (A/B/C/D): ').upper()

            if ans in ['A', 'B', 'C', 'D']:
                if ans == question[5]:
                    crr_ans += 1
                    animation(f'\n✅ RIGHT! The correct answer is {question[5].upper()}!\n')
                    print(f'\n💵 Current Prize Pool: ${prz_per_qst * crr_ans}')
                else:
                    animation(f'\n❌ WRONG! The correct answer was {question[5].upper()}\n')
                    print(f'\n💵 Current Prize Pool: ${prz_per_qst * crr_ans}')    
                    break
                break     
            else:
                animation('\n❌ Invalid input! Enter (A/B/C/D)!\n')
    animation(f'\nNumber of correct answers: {crr_ans}')
    animation(f'\nCongratulations You Have Won: ${prz_per_qst * crr_ans} 🤑\n')

def description():

    print('''
|----------------------------|
|--    GAME DESCRIPTION    --|
|----------------------------|
          
- RULES:

- Enter following to get difficulty of your choice
- 1 -> Easy, 2 -> Medium, 3 -> Hard       
- You will be asked 10 questions in 5 different fields

- PRIZE:
          
- Easy   -> 100 per correct
- Medium -> 200 per correct
- Hard   -> 300 per correct
          

Good luck, challenger!
''')

def intro():
    animation('\n|| *** | ** WELCOME TO MINI QUIZ 2.0 ** | *** ||\n')
