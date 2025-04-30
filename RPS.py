import random

comp_win = 0
user_win = 0
tie = 0
def playGame():
    comp_pick = random.choice(['rock', 'paper', 'scissors'])
    try:
        user_pick = input("Please pick rock, paper, or scissors: ").lower()
    except ValueError:
        print("Invalid input please try again.")
    
    if comp_pick == 'rock' and user_pick == 'scissors' or comp_pick == 'paper'and user_pick == 'rock' or comp_pick == 'scissors' and user_pick == 'paper':
        print(f'Computer picked {comp_pick}')
        print(f'You picked {user_pick}')
        print("you lost this round")
        global comp_win
        comp_win += 1
    elif comp_pick == user_pick:
        print(f'Computer picked {comp_pick}')  
        print(f'You picked {user_pick}')
        print('its a tie')
        global tie
        tie += 1
    else:
        print(f'Computer picked {comp_pick}')
        print(f'You picked {user_pick}')
        print('you win')
        global user_win
        user_win += 1

while True:
    playGame()
    try:
        ask = input('Do you want to play again? (yes/no)').lower()
    except ValueError:
        print("Invalid input please try again.")

    if ask != 'yes':
        print('FInal Score \n')
        print(f'Computer wins: {comp_win} times \n')
        print(f'User wins: {user_win} times\n')
        print(f'Draw: {tie} times\n')
        break