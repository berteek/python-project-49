from random import randint, choice
import brain_games.game as game


def get_question() -> str:
    operation = choice(['+', '-', '*'])
    x = randint(0, 30)
    y = randint(0, 30)
    question = f'{x} {operation} {y}'
    return question


def get_correct_answer(expression: str) -> str:
    x, operation, y = expression.split(' ')
    x = int(x)
    y = int(y)
    match operation:
        case '+':
            return str(x + y)
        case '-':
            return str(x - y)
        case '*':
            return str(x * y)
        case _:
            return ''


def run():
    game_explanation = 'What is the result of the expression?'
    game.run(game_explanation, get_question, get_correct_answer)
