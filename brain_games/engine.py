def welcome_user():
    print('Welcome to the Brain Games!')
    name = input("May I have your name? ")
    print(f'Hello, {name}!')
    return name

def run(game):
    name = welcome_user()
    print(game.DESCRIPTION)
    correct_answers = 0
    while correct_answers < 3:
        correct_answer = 0
        user_answer = ''
        while user_answer != correct_answer:
            question, correct_answer = game.get_question_and_answer()
            print(f'Objective: {question}...')
            user_answer = input("Your answer: ")
            if user_answer == correct_answer:
                print('Correct!')
                correct_answers += 1
                break
            else:
                print(f'{user_answer} is wrong answer... Try again!')
    print(f"Congratulations, {name}!")
