import brain_games.game as game
from random import randint, choice


def get_question() -> str:
    start = randint(0, 30)
    difference = randint(1, 10)
    length = 10
    progression = list(range(start, start + length * difference + 1, difference))
    hidden_number = choice(progression)
    question = ''
    for number in progression:
        if number == hidden_number:
            question += '.. '
        else:
            question += f'{number} '
    return question

def calculate_difference(progression: list[str]) -> int:
    int_streak = 0
    i = 0
    while int_streak < 2:
        if progression[i] == '..':
            int_streak = 0
        else:
            int_streak += 1
        i += 1
    difference = int(progression[i - 1]) - int(progression[i - 2])
    return difference


def calculate_hidden_number(progression: list[str], difference: int) -> int:
    i = 0
    while progression[i] != '..':
        i += 1
    hidden_number = int(progression[i - 1]) + difference if i != 0 else int(progression[i + 1]) - difference
    return hidden_number


def get_correct_answer(progression: str) -> str:
    split_progression = progression.split(' ')
    difference = calculate_difference(split_progression)
    hidden_number = calculate_hidden_number(split_progression, difference)
    return str(hidden_number)


def run():
    game_explanation = 'What number is missing in the progression?'
    game.run(game_explanation, get_question, get_correct_answer)
