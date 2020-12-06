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

# randomly generate play of computer
comp_choice = ['rock', 'paper', 'scissors']
computer1 = random.choice(comp_choice)


# check if valid entry
if play1 not in comp_choice:
    print('You did not make a valid entry. You lose.')
else:
    # display corresponding image
    print(f"You play:\n{game_dict[play1]}")
    print(f"Computer plays:\n {game_dict[computer1]}") 
    # determine winner based on plays 
    if play1 == computer1:
        print('Draw!')
    elif play1 == 'rock':
        if computer1 == 'scissors':
            print('You win.')  
        print('Computer wins.')
    elif play1 == 'scissors':
        if computer1 == 'paper':
            print('You win.')
        print('Computer wins.')
    elif play1 == 'paper':
        if computer1 == 'rock':
            print('You win')
        print('Computer wins.')
