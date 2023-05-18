#!/usr/bin/python3

class Questions:
    
    _total = 0
    _total_questions = 0
    
    def __init__(self,question,answer,letter):
        self._question = question
        self._answer = answer
        self._letter = letter
        self._choices = []
        Questions._total_questions += 1

    def get_results():
        return Questions._total

    def get_total():
        return Questions._total_questions

    def get_question(self):
        return input(self._question)
    
    def get_answer(self):
        return self._answer
    
    def get_letter(self):
        return self._letter     
    
    def add_choices(self,**kwargs):
        for key,value in kwargs.items():
            self._choices += {key:value},
    
    def get_choices(self):
        print()
        for i in self._choices:
            for key,value in i.items():
                print('{}.) {}'.format(key,value))
        print()

    def correct():
        Questions._total += 1

def answer_checker(value):

    if value.isalpha() == True:
        value = value.upper()

    match value:
        case '1'|'A':
            return 'A'
        case '2'|'B':
            return 'B'
        case '3'|'C':
            return 'C'
        case '4'|'D':
            return 'D'
        case _:
            print('\nInvalid choice!\nPlease choose between the options listed below.')
            return 'invalid'

question_1 = Questions('Who created Python?: ','Guido van Rossum','A')
question_1.add_choices(A='Guido van Rossum',B='Elon Musk',C='Bill Gates',D='Mark Zuckerburg')

question_2 = Questions('What year was Python Created?: ','1991','B')
question_2.add_choices(A='1989',B='1991',C='2000',D='2018')

question_3 = Questions('Python is tributed with which comedy group: ','Monty Python','C')
question_3.add_choices(A='Lonely Island',B='Smoth',C='Monty Python',D='SNL')

question_4 = Questions('Is the earth round?: ','True','A')
question_4.add_choices(A='True',B='False',C='Sometimes',D='What\'s Earth??')

my_questions = (question_1,question_2,question_3,question_4)

for i in my_questions:
    is_valid = None
    while is_valid == None or is_valid == 'invalid':
        i.get_choices()
        is_valid = answer_checker(i.get_question())
    if is_valid == i.get_letter():
        print('\nYou choose ({}) {} which is the correct answer!'.format(is_valid,i.get_answer()))
        Questions.correct()
    else:
        print('\n{} is incorrect, the answer was ({}) {}.'.format(is_valid,i.get_letter(),i.get_answer()))
    print('____________________________________________________________________')

print('\nResults: {} / {}\n____________________________________________________________________\n'\
      .format(Questions.get_results(),Questions._total_questions))