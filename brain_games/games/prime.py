from random import randint

DESCRIPTION = "Answer 'yes' if given number is prime, otherwise answer 'no'."

def prime_check(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def get_question_and_answer():
    num = randint(0, 100)
    question = f'{num} is prime?'
    answer = 'yes' if prime_check(num) else 'no'
    return question, answer
