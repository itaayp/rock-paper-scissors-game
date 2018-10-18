from random import randint

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

pc = randint(0,2)
if pc == 0:
    pc = "rock"
elif pc == 1:
    pc = "paper"
else:
    pc = "scissors"
input("The computer plays: " + pc)

if p1 == 'rock' or p1 == 'paper' or p1 == 'scissors': # verify if p1 typed a valid word
    if p1 == pc:
        print("IT'S A TIE!!")
    elif p1 == "rock" and pc == "scissors":
        print("PLAYER 1 WINS!!")
    elif p1 == "paper" and pc == "rock":
        print("PLAYER 1 WINS!!")
    elif p1 == "scissors" and pc == "paper":
        print("PLAYER 1 WINS!!")
    else:
        print("PLAYER 2 WINS!!")
else:
    print("P1, YOU MUST TO TYPE A VALID WORD!")
