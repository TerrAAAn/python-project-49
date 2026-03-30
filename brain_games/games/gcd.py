import math
from random import randint

DESCRIPTION = "Let's find the GCD between two numbers"  

def get_question_and_answer():
    number_1, number_2 = randint(0, 100), randint(0, 100)
    answer = str(math.gcd(number_1, number_2))
    question = f'the largest common divisor between the {number_1} and {number_2}'
    return question, answer