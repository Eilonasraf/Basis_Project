import random
import Players
import logging
from random import choice
def R_P_S (name):
        print("Welcome to Paper,Rock or Scissors Game")
        user_wins = 0
        computer_wins = 0
        list_of_options = ["Rock", "Paper", "Scissors"]
        User_selection = input("Enter your choose:\n")
        Computer_selection = random.choice(list_of_options)
        while User_selection != "Leave":
            if User_selection == "Scissors":
                if Computer_selection != "Rock":
                    user_wins += 1
                else:
                    computer_wins += 1

            elif User_selection == "Paper":
                if Computer_selection != "Scissors":
                    user_wins += 1
                else:
                    computer_wins += 1

            elif User_selection == "Rock":
                if Computer_selection != "Paper":
                    user_wins += 1
                else:
                    computer_wins += 1
            User_selection = input("Enter your choose:\n")
            Computer_selection = random.choice(list_of_options)

        if user_wins == 0 and computer_wins == 0:
            return 0

        if user_wins >= computer_wins:
            return 1
        else:
            return 0
