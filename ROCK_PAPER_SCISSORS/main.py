import random


def get_computer_choice():
    """Generates a random choice for the computer (Rock, Paper, Scissors)."""
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)
    # Use random.choice directly for elements from a list


def get_user_choice():
    """
    Prompts the user for their choice and validates it.
    Keeps prompting until a valid choice is entered.
    """
    valid_choices = ["rock", "paper", "scissors"]
    while True:
        user_input = input("Enter your choice (Rock, Paper, or Scissors): ").lower()
        if user_input in valid_choices:
            return user_input.capitalize()
            # Return with first letter capitalized for consistent display
        else:
            print("Invalid choice. Please type 'Rock', 'Paper', or 'Scissors'.")


def determine_winner(user_choice, computer_choice):
    """Determines the winner of a single round."""
    print(f"\nYou Chose: {user_choice}")
    print(f"Computer Chose: {computer_choice}\n")

    if user_choice == computer_choice:
        return "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "You Win!"
    else:
        return "Computer Wins!"


def main():
    """Main function to run the Rock, Paper, Scissors game."""
    print("=" * 50)
    print("        Welcome to Rock, Paper, Scissors")
    print("=" * 50)

    # Validate initial game start input
    while True:
        game_start_input = input("Do you want to start the game? (yes/no): ").lower()
        if game_start_input in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

    if game_start_input == "no":
        print("Okay, maybe next time! Goodbye.")
        return
        # Exit the main function if user doesn't want to play

    user_score = 0
    computer_score = 0
    round_number = 0

    while True:
        # Main game loop for continuous play
        round_number += 1
        print(f"\n--- Round {round_number} ---")

        user_move = get_user_choice()
        # Get user choice ONCE per round
        computer_move = get_computer_choice()
        # Get computer choice ONCE per round

        result = determine_winner(user_move, computer_move)
        print(result)

        # Update scores
        if result == "You Win!":
            user_score += 1
        elif result == "Computer Wins!":
            computer_score += 1

        print(f"Score: You {user_score} - Computer {computer_score}")

        # Ask to play another round
        while True:
            play_again = input("\nPlay another round? (yes/no): ").lower()
            if play_again in ["yes", "no"]:
                break
            else:
                print("Invalid input. Please type 'yes' or 'no'.")

        if play_again == "no":
            print("\n" + "=" * 50)
            print("         Game Over!")
            print(f"         Final Score: You {user_score} - Computer {computer_score}")
            if user_score > computer_score:
                print("         Congratulations! You are the overall winner!")
            elif computer_score > user_score:
                print("         Better luck next time! The Computer won overall.")
            else:
                print("         It's an overall tie!")
            print("=" * 50)
            break
            # Exit the main game loop

# Standard practice to run the main function


if __name__ == "__main__":
    main()
