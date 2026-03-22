import random

options = ("rock","paper","scissor")
player = None 
computer = random.choice(options)

playing = True
while playing:
    while player not in options:
       player = input("Enter a Choice :(rock , paper , scissor) : ")
    print(f"Player : {player}")
    print(f"Computer : {computer}")

    if player == computer:
        print("Its Tie")
    elif player == "rock" and computer == "scissor":
        print("Win")
    elif player == "paper" and  computer == "rock":
        print("win")
    elif player == "scissor" and  computer == "paper":
        print("win")
    else : 
        print("You Lose ")
    playing = False
print("thanks For Playing ..........")