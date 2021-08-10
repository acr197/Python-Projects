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

import random

choices = ["rock", "paper", "scissors"]
user_choice = input("Pick One: Rock, Paper, Scissors\n").lower()

if user_choice == "rock":
  print(rock)
if user_choice == "scissors":
  print(scissors)
if user_choice == "paper":
  print(paper)

comp_choice = random.randint(0,2)
if comp_choice == 0:
  print(rock)
if comp_choice == 1:
  print(scissors)
if comp_choice == 2:
  print(paper)

if user_choice == "rock" and comp_choice == 0:
  print("Draw")
elif user_choice == "scissors" and comp_choice == 1:
  print("Draw")
elif user_choice == "paper" and comp_choice == 2:
  print("Draw")
elif user_choice == "rock" and comp_choice == 1:
  print("You Win!")
elif user_choice == "scissors" and comp_choice == 2:
  print("You Win!")
elif user_choice == "paper" and comp_choice == 0:
  print("You Win!")
else:
  print("You Suck!")




