import random

def guess():
    number = random.randint(1, 100)
    guess = 0

    while guess != number:
        guess = int(input("Enter Guess: "))
        if guess < number:
            print("Guess higher!")
        elif guess > number:
            print("Guess lower!")
        else:
            print("successful", number)

def rock_paper_scissors():
    options = ("rock", "paper", "scissors")
    running = True

    while running:
        player = None
        computer = random.choice(options)
        while player not in options:
            player = input("choose (rock, paper, scissors): ")

        print(f"Player: {player}")
        print(f"Computer: {computer}")

        if player == computer:
            print("draw!!!")
        elif player == "rock" and computer == "scissors":
            print("victory!")
        elif player == "paper" and computer == "rock":
            print("victory!")
        elif player == "scissors" and computer == "paper":
            print("victory!")
        else:
            print("defeat!")

        play_again = input("having fun? wanna Play again? (y/n): ").lower()
        if play_again != "y":
            running = False

    print("well played, thanks for the fun!")

def main():
    while True:
        print("\nMenu:")
        print("1. Guess a Number")
        print("2. Rock Paper Scissors")
        print("3. Exit")

        choice = input("choose b/w (1-3): ")

        if choice == '3':
            guess()
        elif choice == '1':
            rock_paper_scissors()
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print(" Please try again.")

if __name__ == "__main__":
    main()