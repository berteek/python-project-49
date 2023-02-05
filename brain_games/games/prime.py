import brain_games.game as game
from random import getrandbits, choice


def is_prime(number: int) -> bool:
    if number == 2 or number == 3:
        return True
    if number % 2 == 0 or number < 2:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


def get_random_prime(start: int, finish: int) -> int:
    primes = [i for i in range(start, finish) if is_prime(i)]
    prime = choice(primes)
    return prime


def get_random_not_prime(start: int, finish: int) -> int:
    numbers = [i for i in range(start, finish) if not is_prime(i)]
    number = choice(numbers)
    return number


def get_question() -> str:
    is_answer_prime = getrandbits(1)
    start = 0
    finish = 30
    number = (get_random_prime(start, finish)
              if is_answer_prime
              else get_random_not_prime(start, finish))
    return str(number)


def get_correct_answer(number: str) -> str:
    return 'yes' if is_prime(int(number)) else 'no'


def run() -> None:
    game_explanation = ('Answer "yes" if given number is prime. '
                        'Otherwise answer "no".')
    game.run(game_explanation, get_question, get_correct_answer)
