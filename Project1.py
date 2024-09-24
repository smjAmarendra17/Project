import random

def guessing_game():
    number_to_guess = random.randint(1, 10)
    attempts = 5

    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")
    print(f"You have {attempts} attempts to guess the number.\n")

    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} correctly!")
            break
    else:
        print(f"Sorry, you've used all {attempts} attempts. The number was {number_to_guess}.")

if __name__ == "__main__":
    guessing_game()
    