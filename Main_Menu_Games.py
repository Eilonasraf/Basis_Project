import RPS
import Players
from Players import Player
import H_man
from H_man import Hangman
import logging
from random_word import RandomWords
# name = input("Hi,Enter your name\n""If you are not interested in playing, please enter the word - Leave\n")
print("-----Main Menu-----")
print("Hi, please choose one of the following options:\n")
print("1 - Rock,Paper,Scissors\n"+"2 - Hangman\n"+"3 - Another user\n"+"4 - Quit")
my_name = Player()
choose = int(input("Enter your selection number to play\n"))
List1 = [0, 0, 0]
counter1 = 0
logging.basicConfig(filename="test.log", level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
while choose != 4:
    if choose == 3:
        my_name = Player()
        choose = int(input("Enter your selection number to play\n"))
    while choose == 1:
                number_of_wins_in_one = my_name.data_c(my_name)
                my_name.all_the_data(number_of_wins_in_one, counter1, List1)
                logging.info('Name : {}, wins numbers in RPS: {}'.format(my_name.new_name, number_of_wins_in_one,))
                choose = int(input("Enter your selection number to play\n"))

    while choose == 2:
                number_of_wins_in_two = my_name.data_hang(my_name)
                if number_of_wins_in_two == 1:
                    List1[1] = number_of_wins_in_two + 1
                elif List1[1] > 0:
                    List1[1] = number_of_wins_in_two - 1
                logging.info('Name : {}, wins numbers in RPS: {}'.format(my_name.new_name, number_of_wins_in_two, ))
                choose = int(input("Enter your selection number to play\n"))

    if choose == 3:
              with open("file.data", "a") as pointer:
                    pointer.write("Status of:" + " " + str(my_name.new_name))
                    pointer.write("\n")
                    pointer.write("The numbers of wins in Rock, Paper or Scissors is:" + str(List1[0]) + "\n")
                    pointer.write("The numbers of wins in Hangman is:" + str(List1[1]))
                    pointer.write("\n")
              for i in range(2):
                List1[0] = 0


