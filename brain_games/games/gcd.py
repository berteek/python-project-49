import brain_games.game as game
import math
from random import randint


def get_question() -> str:
    x = randint(0, 30)
    y = randint(0, 30)
    question = f'{x} {y}'
    return question


def get_correct_answer(numbers: str) -> str:
    x, y = numbers.split(' ')
    x = int(x)
    y = int(y)
    gcd = math.gcd(x, y)
    return str(gcd)


def run() -> None:
    game_explanation = 'Find the greatest common divisor of given numbers.'
    game.run(game_explanation, get_question, get_correct_answer)
