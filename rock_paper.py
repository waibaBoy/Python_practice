import random

computer_choice = random.choice(['rock', 'paper', 'scissors'])
user = input("Enter your choice (rock, paper, scissors): ")
if user == computer_choice:
    print('Its a tie!')
elif user == 'rock' and computer_choice == 'scissors' or user == 'paper' and computer_choice == 'rock' or user == 'scissors' and computer_choice == 'paper':
    print('You win!')
else:   
    print('You lost!')
print(f'Computer chose {computer_choice}')
# This code implements a simple rock-paper-scissors game where the user plays against the computer.