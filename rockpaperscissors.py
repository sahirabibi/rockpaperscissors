# a simple rock paper scissors game

import random

# ascii images for each play
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# dictionary to pull store ascii images in
game_dict = {'rock': rock, 'paper': paper, 'scissors': scissors}

# ask player to pick their play
play1 = input('Pick your play:\nrock\npaper\nscissors\n\n')
# print corressponding image from game_dict
print(f"You play:\n{game_dict[play1]}")

# randomly generate play of computer
comp_choice = ['rock', 'paper', 'scissors']
computer1 = random.choice(comp_choice)
# display corresponding image
print(f"Computer plays:\n {game_dict[computer1]}")

# determine winner based on plays
if play1 == computer1:
    print('Draw!')
elif play1 == 'rock':
    if computer1 == 'scissors':
        print('You win.')
    elif computer1 == 'paper':
        print('Computer wins.')
elif play1 == 'scissors':
    if computer1 == 'paper':
        print('You win.')
    elif computer1 == 'rock':
        print('Computer wins.')
elif play1 == 'paper':
    if computer1 == 'rock':
        print('You win')
    elif computer1 == 'scissors':
        print('Computer wins.')
