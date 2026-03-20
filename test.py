from brain_games import engine

class TestGame:
    DESCRIPTION = "What is the result of the expression?"
    @staticmethod
    def get_question_and_answer():
        return "2 + 2", "4"   

engine.run(TestGame())
