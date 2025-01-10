import random

def main():
    print("Welcome to the Number Guessing Game!")
    print("I've picked a random number between 1 and the specified range.")
    print("Your task is to guess the number. Let's get started!")

    # Get the range from the user
    try:
        range_max = int(input("Enter the maximum value for the range: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    # Generate a random number within the specified range
    secret_number = random.randint(1, range_max)

    # Initialize variables
    guesses = []
    guess = None

    # Main game loop
    while guess != secret_number:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if guess > secret_number:
            print("Too high! Try a lower number.")
        elif guess < secret_number:
            print("Too low! Try a higher number.")

        guesses.append(guess)

    print(f"Congratulations! You guessed the number {secret_number} correctly.")
    print(f"Your guesses: {', '.join(map(str, guesses))}")

if __name__ == "__main__":
    main()