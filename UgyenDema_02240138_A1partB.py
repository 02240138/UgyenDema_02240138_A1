# Import the random module for generating random numbers
import random

# Function to play "Guess a Number"
def guess():
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    guess = 0  # Initialize the guess variable

    # Keep asking the user for guesses until the guess is correct
    while guess != number:
        guess = int(input("Enter Guess: "))  # Ask the user for their guess
        if guess < number:
            print("Guess higher!")  # Hint to guess higher
        elif guess > number:
            print("Guess lower!")  # Hint to guess lower
        else:
            print("Successful! The number was", number)  # When the user guesses correctly

# Function to play "Rock, Paper, Scissors"
def rock_paper_scissors():
    # Define the possible choices for the game
    options = ("rock", "paper", "scissors")
    running = True  # Set the game to run

    while running:
        player = None  # Initialize player's choice as None
        computer = random.choice(options)  # Randomly choose the computer's move
        
        # Keep asking the player for a valid move until they provide one
        while player not in options:
            player = input("Choose (rock, paper, scissors): ").lower()  # Convert player input to lowercase

        print(f"Player: {player}")
        print(f"Computer: {computer}")

        # Determine the winner based on the rules of the game
        if player == computer:
            print("Draw!")  # Both player and computer choose the same move
        elif player == "rock" and computer == "scissors":
            print("Victory!")  # Player wins with rock against scissors
        elif player == "paper" and computer == "rock":
            print("Victory!")  # Player wins with paper against rock
        elif player == "scissors" and computer == "paper":
            print("Victory!")  # Player wins with scissors against paper
        else:
            print("Defeat!")  # Player loses

        # Ask the player if they want to play again
        play_again = input("Having fun? Wanna play again? (y/n): ").lower()
        if play_again != "y":
            running = False  # Stop the game if the player doesn't want to play again

    print("Well played, thanks for the fun!")  # End the game

# Main function to display the menu and handle user input
def main():
    while True:
        # Display the menu with options
        print("\nMenu:")
        print("1. Guess a Number")
        print("2. Rock Paper Scissors")
        print("3. Exit")

        # Ask the user to choose an option
        choice = input("Choose between (1-3): ")

        # Handle the user's choice
        if choice == '1':
            guess()  # Start the "Guess a Number" game
        elif choice == '2':
            rock_paper_scissors()  # Start the "Rock Paper Scissors" game
        elif choice == '3':
            print("Exiting...")  # Exit the program
            break
        else:
            print("Please try again.")  # In case of invalid input

# This line ensures that the program runs when executed as a script
if __name__ == "__main__":
    main()  # Call the main function to start the program
