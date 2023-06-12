#!/usr/bin/python3

def answer_checker(value,answer,key):

    def return_answer(value,answer,key):
        if value == True:
            print('\nthats correct! The answer was ('+answer+'):',key)
        elif value == False:
            print('\nthat is incorrect, the answer was ('+answer+'):',key)

    def check_answer(answer,choice):
        if answer == choice:
            return_answer(True,answer,key)
            return 1
        else:
            return_answer(False,answer,key)
            return 0

    if value.isalpha() == True:
        value = value.upper()
    
    match value:
        case '1'|'A':
            return check_answer(answer,'A')
        case '2'|'B':
            return check_answer(answer,'B')
        case '3'|'C':
            return check_answer(answer,'C')
        case '4'|'D':
            return check_answer(answer,'D')
        case _:
            print('\ninvalid choice!\n')
            return 'invalid'

def new_game():
    score = num = total = 0
    answer_key = answer_keys = ''
    for question_key,question_value in questions.items():
        if total == 0:
            total = questions.__len__()
        answer = None
        while answer == None or answer == 'invalid':
            for i in options[num]:
                for j_key,j_value in i.items():
                    if j_value == str(question_value+')') and answer != 'invalid':
                        answer_keys = answer_keys+'\n'+str(int(num+1))+'): '+j_key
                        answer_key = j_key
                    print(str(j_value),str(j_key))
            answer = answer_checker(input('\n'+question_key),question_value,answer_key)
        score += answer
        num += 1
        print('_______________________________________________\n')
    print('Score:',score,'/',str(total)+'\n_______________________________________________')
    print(answer_keys+'\n_______________________________________________\n')

questions = {
    'Who created Python?: ':'A',
    'What year was Python Created?: ':'B',
    'Python is tributed with which comedy group: ':'C',
    'Is the earth round?: ':'A'
}

A,B,C,D = 'A)','B)','C)','D)'
answers = [A,B,C,D]

options = [
    [{'Guido van Rossum':A},{'Elon Musk':B},{'Bill Gates':C},{'Mark Zuckerburg':D}],
    [{'1989':A},{'1991':B},{'2000':C},{'2018':D}],
    [{'Lonely Island':A},{'Smoth':B},{'Monty Python':C},{'SNL':D}],
    [{'True':A},{'False':B},{'Sometimes':C},{'What\'s Earth?':D}],
]

new_game()