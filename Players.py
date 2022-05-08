import H_man
import RPS
import logging
from random_word import RandomWords
class Player:
    def __init__(self):
        self.new_name = input("Enter your name please\n")
        print("If you are not interested in this game, type the word - Leave")
        self.items = []

    def data_c (self, new_name):
        win_or_lose = 0
        win_or_lose = RPS.R_P_S(new_name)
        return win_or_lose

    def data_hang(self, new_name):
        w_o_l = 0
        w_o_l = H_man.Hangman(new_name)
        return w_o_l

    def all_the_data(self, number, counter1, List1):
        if number == 1:
            counter1 += 1
            List1[0] = List1[0] + counter1
        elif List1[0] > 0:
            List1[0] = List1[0] - 1
            return List1


