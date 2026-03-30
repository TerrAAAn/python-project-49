from random import randint

DESCRIPTION = "Find the hidden element of the list."

def get_question_and_answer():
    start = randint(1, 100)
    step = randint(1, 10)
    stop = start + (10)*step
    progression = list(range(start, stop, step))
    hidden = randint(0, len(progression)-1)
    answer = str(progression[hidden])
    progression[hidden] = '...'
    question = ' '.join(str(num) for num in progression)
    return question, answer


