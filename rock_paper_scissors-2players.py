print("")
print("")
print("WELCOME TO THE ROCK, PAPER, SCISSORS GAME!!")

print("")
print("...rock...")
print("...paper...")
print("...scissors...")

print("")
print("")
p1 = input("Player 1: It's your time: ").lower()
print("NO CHEATING! \n\n" *25)
p2 = input("Player 2: It's your time: ").lower()


if p1 == 'rock' or p1 == 'paper' or p1 == 'scissors':        # verify if p1 typed a valid word
    if p2 == 'rock' or p2 == 'paper' or p2 == 'scissors':    # verify if p2 typed a valid word
        if p1 == p2:
            print("IT'S A TIE!!")
        elif p1 == "rock" and p2 == "scissors":
            print("PLAYER 1 WINS!!")
        elif p1 == "paper" and p2 == "rock":
            print("PLAYER 1 WINS!!")
        elif p1 == "scissors" and p2 == "paper":
            print("PLAYER 1 WINS!!")
        else:
            print("PLAYER 2 WINS!!")
    else:
        print("P2, YOU MUST TO TYPE A VALID WORD!")
else:
    print("P1, YOU MUST TO TYPE A VALID WORD!")
