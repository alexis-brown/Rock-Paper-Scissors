from random import randint

# Play options
t = ["Rock", "Paper", "Scissors"]

# Random play from the computer
computer = t[randint(0, 2)]

player = False

while player == False:
    player = input("Rock, Paper, Scissors? ")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose! " + computer + " covers " + player)
        else:
            print("You win! " + player + " smashes " + computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose! " + computer + " cuts " + player)
        else:
            print("You win! " + player + " covers " + computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose! " + computer + " smashes " + player)
        else:
            print("You win! " + player + " cuts " + computer)
    else:
        print("That was not a valid play. Check your spelling.")

    player = False
    computer = t[randint(0, 2)]