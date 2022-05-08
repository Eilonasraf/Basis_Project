def Hangman (name):
    import random
    import string
    from random_word import RandomWords
    import logging
    from random import choice
    Separated_string = []
    Good_guess = []
    x = '_'
    counter_wins = 0
    counter_los = 0
    print("Welcome to Hangman Game")
    letters = RandomWords()
    The_word = letters.get_random_word()
    number_of_guesses = len(The_word)
    for i in range(number_of_guesses):
        Good_guess.append('_')
    for i in range(number_of_guesses):
        Separated_string.append(The_word[:1])
        The_word = The_word[1:]
    for i in range(number_of_guesses):
        User_guess = input("Enter the selection of the letter you selected:\n")
        if x not in Good_guess:
            return 1
        if User_guess in Separated_string:
                for j in range (len(Separated_string)):
                    if Separated_string[j] == User_guess:
                        Good_guess[j] = Separated_string[j]
                counter_wins += 1
                number_of_guesses -= 1
                print("Very good,but you have more:", number_of_guesses , "guesses")
                print(Good_guess)
        else:
            counter_los += 1
            number_of_guesses -= 1
            print("Sorry, wrong guess…you have more", number_of_guesses, "guesses")
            print(Good_guess)

    if x in Good_guess:
        return 0
    else:
        return 1

