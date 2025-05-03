import random

comp_score = 0
user_score = 0
draws = 0
def number_battle():
    comp_num = random.randint(1, 100)
    user_num = random.randint(1, 100)
    if comp_num > user_num:
        print(f'Computer got: {comp_num}')
        print(f'you got:  {user_num}')
        print('you lost this round')
        global comp_score
        comp_score += 1
    elif comp_num < user_num:
        print(f'Computer got: {comp_num}')
        print(f'you got:  {user_num}')
        print('you win this round')
        global user_score
        user_score += 1
    else:
        print(f'Its a draw: {comp_num} = {user_num}')
        global draws
        draws += 1


while True:
    number_battle()
    ask = input('Do you want to play again: y/n?\n').lower()
    if ask != 'y':
        print('Final Score \n')
        print(f'Computer wins: {comp_score} times \n')
        print(f'User wins: {user_score} times\n')
        print(f'Draw: {draws} times\n')
        break   



