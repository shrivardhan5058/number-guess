"""Number Guess: the player guesses a number chosen by the computer."""

import random

def main():
    number = random.randint(1, 100)
    guesses = 0

    print("I am thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Guess the number: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if not 1 <= guess <= 100:
            print("Please enter a number between 1 and 100.")
            continue

        guesses += 1

        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        else:
            print(f"Correct! You guessed the number in {guesses} guesses.")
            break

if __name__ == "__main__":
    main()
