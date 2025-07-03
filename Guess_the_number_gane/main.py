import random


def guess_the_number_game():

    # It's good practice to wrap your game logic in a function
    # 1. Computer generates a random number
    computer_number = random.randint(1, 10)

    # Corrected: use random.randint(start, end)
    print("I have chosen a number between 1 and 10. Can you guess it?")

    attempts = 0

    # Initialize a counter for attempts
    while True:

        # Loop indefinitely until the user guesses correctly
        attempts += 1
        try:

            # Use a try-except block to handle invalid input
            # 2. Get user input
            user_guess = int(input("What number do you think I chose? "))

            # Corrected: int() around input()
        except ValueError:
            print("That's not a valid number. Please enter an integer.")
            continue

            # Go back to the start of the loop

        # 3. Compare numbers and provide feedback
        if user_guess == computer_number:
            print(f"Yes! The number was {computer_number}."
                  f" You guessed it in {attempts} attempts!")

            # Use f-strings for easy formatting
            print("Congratulations!")
            break

            # Exit the loop if the guess is correct
        elif user_guess < computer_number:

            # Use elif for "else if"
            print("Too low! Try a higher number.")
        else:

            # The only remaining possibility is user_guess > computer_number
            print("Too high! Try a lower number.")


# Call the function to start the game
guess_the_number_game()
