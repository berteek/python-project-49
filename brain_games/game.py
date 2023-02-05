from typing import Callable
import prompt


def get_player_name() -> str:
    name = str(prompt.string('May I have your name? '))
    print(f'Hello, {name}!')
    return name


def ask_player_questions(
        game_explanation: str,
        get_question: Callable[[], str],
        get_correct_answer: Callable[[str], str]
) -> bool:
    """Returns True if player answered correctly, otherwise returns False."""

    print(game_explanation)
    for _ in range(3):
        question = get_question()
        correct_answer = get_correct_answer(question)
        print(f'Question: {question}')
        player_answer = str(prompt.string('Your answer: '))

        if player_answer != correct_answer:
            print(f'\'{player_answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{correct_answer}\'')
            return False
        print('Correct!')
    return True


def run(
        game_explanation: str,
        get_question: Callable[[], str],
        get_correct_answer: Callable[[str], str]
) -> None:
    print('Welcome to the Brain Games! ')

    name = get_player_name()

    did_player_answer_correctly = ask_player_questions(
        game_explanation,
        get_question,
        get_correct_answer)

    if did_player_answer_correctly:
        print(f'Congratulations, {name}!')
    else:
        print(f'Let\'s try again, {name}!')
