from random import randint
import prompt


def get_player_name() -> str:
    name = str(prompt.string('May I have your name? '))
    print(f'Hello, {name}!')
    return name

def is_even(number: int) -> str:
    return 'yes' if number % 2 == 0 else 'no'

def ask_player_questions() -> bool:
    """Returns True if player answered correctly, otherwise returns False."""
    
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        number = randint(0, 30)
        correct_answer = is_even(number)
        
        print(f'Question: {number}')
        player_answer = str(prompt.string('Your answer: '))
        
        if player_answer != correct_answer:
            return False
        print('Correct!')
    return True

def run() -> None:
    print('Welcome to the Brain Games!' )

    name = get_player_name()
    
    did_player_answer_correctly = ask_player_questions()
    if did_player_answer_correctly:
        print(f'Congratulations, {name}!')
    else:
        print(f'Let\'s try again, {name}!')
