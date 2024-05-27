import random

options = ("Rock", "Paper", "Scissors")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (Rock, Paper, Scissors): ")

    print(f"player: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("It's a Tie!")
    elif player == "Rock" and computer == "Scissors":
        print("You Win!")
    elif player == "Paper" and computer == "Rock":
        print("You Win!")
    elif player == "Scissors" and computer == "Paper":
        print("You Win!")
    elif player == "Rock" and computer == "Paper":
        print("You Lose!")
    elif player == "Paper" and computer == "Scissors":
        print("You Lose!")
    elif player == "Scissors" and computer == "Rock":
        print("You Lose!")
    else:
        print("You Lose!")

    play_again = input("Play again? (y/n): ").lower()
    if not play_again == "y":
        running = False

    print("Thanks for playing!")
