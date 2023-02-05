from random import randint
import brain_games.game as game


def is_even(number: int) -> str:
    return 'yes' if number % 2 == 0 else 'no'


def get_correct_answer(number: str) -> str:
    correct_answer = is_even(int(number))
    return correct_answer


def get_question() -> str:
    number = randint(0, 30)
    return str(number)


def run():
    game_explanation = ('Answer "yes" if the number is even, '
                        'otherwise answer "no".'
                        )
    game.run(game_explanation, get_question, get_correct_answer)
