#!/usr/bin/python3

import random # this is a the module in python 

COURSE_CODE = 'CST8245' # const value
course_number = random.randint(1,10) # generates a random section number between 1 and 10
begin_game = True # the condition that continues and begins the game  

def check_answer(guess):
    if guess.isnumeric(): # checks if the value is numeric, if it is the value will be returned true begin_guessing()
        return int(guess)
    else:
        return 0 # must return a numeric value, if 0 is returned the user entered something else

def begin_guessing(guess_count): # loops indefinitely until user chooses correctly
    while check_answer(input("guess your course number: ")) != course_number: # if the user guessed correctly the while loop terminates
        guess_count = guess_count + 1 # add 1 to guess_count for each time the loop conpletes a cycle which is completed after a user enters their guess
        print(f"your current guess count is {guess_count}") # if the user guessed incorrectly they will have their guess count displayed for that round
        continue # continue restarts loops

def play_game(answer): # exits the game if answer is y yes or true
    if answer.upper() in ['Y','YES','1']:
        return True # the default is to return nothing which will break to loop
    else:
        print("Thank you")

def main(begin_game): # main function
    while begin_game:
        guess_count = 0 # keeps track of the number of guesses the user makes
        begin_guessing(guess_count)
        print('You guessed correctly, your section number for {} is infact {}.'.format(COURSE_CODE,course_number))
        begin_game = play_game(input("play again? (y)es or (n)o: "))  # checks if the user wants to play again

if play_game(input("are you ready to start? (y)es or (n)o: ")) == True: # double checks if the user really wants to begin
    main(begin_game)
