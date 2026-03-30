from random import randint

DESCRIPTION = "What is the result of the expression?"

def get_question_and_answer():
    num_1 , num_2 = randint(1, 50), randint(1, 50)
    operand_array = ['+', '-', '*']
    operand = operand_array[randint(0, len(operand_array)-1)]
    question = f'{num_1} {operand} {num_2}'
    match operand:
        case '+':
            answer = str(num_1 + num_2)
        case '-':
            answer = str(num_1 - num_2)
        case '*':
            answer = str(num_1 * num_2)
    return question, answer
