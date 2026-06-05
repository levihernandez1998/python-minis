import art
import random

HARD_LEVEL = 5
EASY_LEVEL = 10

chosen_number = 0
number_of_guesses = 0

def start():
    print(art.logo)
    print("I'm thinking of a number between 1 and 100.")

    global chosen_number
    global number_of_guesses
    chosen_number = random.randint(1, 100)
    print(f"Psssst! It's {chosen_number}.")

    while number_of_guesses == 0:
        number_of_guesses = get_number_of_guesses()

    is_guessed = make_a_guess()
    while not is_guessed and number_of_guesses > 0:
        is_guessed = make_a_guess()

    if is_guessed:
        print(art.win)
    else:
        print(art.lose)

    another_round = input("Do you want to play again? (y/n): ")
    if another_round.lower() == "y":
        print("\n"*20)
        start()

def get_number_of_guesses():
    difficulty = input("Choose a difficulty level ('easy' or 'hard'): ")
    if difficulty.lower() == "easy":
        return EASY_LEVEL
    elif difficulty.lower() == "hard":
        return HARD_LEVEL
    else:
        print("Please choose a difficulty level.")
        return 0

def make_a_guess():
    global chosen_number
    global number_of_guesses

    print(f"You have {number_of_guesses} to guess the number.")
    guess = int(input("Make a guess: "))

    number_of_guesses -= 1
    if guess == chosen_number:
        return True
    else:
        if chosen_number > guess:
            print("Higher!")
        else:
            print("Lower!")
        return False

start()