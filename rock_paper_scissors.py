#!/usr/bin/python3

import random

def valid_choice(value):
    if value.isalpha() == True:
        value = value.upper()

    match value:
        case '1'|'ROCK'|'R':
            return 'Rock'
        case '2'|'PAPER'|'P':
            return 'Paper'
        case '3'|'SCISSORS'|'S':
            return 'Scissors'
        case _:
            print('\ninvalid choice!\n')

def winner(c,p):
    the_winner = '\nthe {} beat the {} with {}.\n'
    cw = the_winner.format('Computer','Player',c)
    pw = the_winner.format('Player','Computer',p)
    if c == p:
        return '\nthe game ends in a tie.\n'
    elif c == 'Rock':
        if p == 'Paper':
            return pw
        else:
            return cw   
    elif c == 'Paper':
        if p == 'Scissors':
            return pw
        else:
            return cw        
    else:
        if p == 'Rock':
            return pw
        else:
            return cw

computer = player = None
choices = ['Rock','Paper','Scissors']
computer = random.choice(choices)
while player not in choices:
    player = valid_choice(input('please choose between rock, paper or scissors: '))
print('\nComputers Choice:',computer)
print('Players Choice:',player)
print(winner(computer,player))