import random

choices = ["rock", "paper", "scissors"]
running = True

while running:

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Choose rock, paper or scissors: ").lower()

    if player == computer:
        print("Computer: " + computer)
        print("Player: " + str(player))
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("Computer: " + computer)
            print("Player: " + str(player))
            print("You lose!")
        elif computer == "scissors":
            print("Computer: " + computer)
            print("Player: " + str(player))
            print("You win!")
    elif player == "scissors":
        if computer == "paper":
            print("Computer: " + computer)
            print("Player: " + str(player))
            print("You win!")
        elif computer == "rock":
            print("Computer: " + computer)
            print("Player: " + str(player))
            print("You lose!")
    elif player == "paper":
        if computer == "scissors":
            print("Computer: " + computer)
            print("Player: " + str(player))
            print("You lose!")
        elif computer == "rock":
            print("Computer: " + computer)
            print("Player: " + str(player))
            print("You win!")

    play_again = input("Do you wanna play again? (yes/no): ")

    if play_again != "yes":
        break

print("Bye! :)")

