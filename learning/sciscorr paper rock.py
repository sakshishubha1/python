import random
choices=["rock","paper","scissors "]
player=input("choose between rock paper and scciors")
ai=random.choice(choices)
print("you chose",player)
print("Ai chose",ai)
if player==ai:
    print("draw")
elif player=="rock" and ai=="scissors":
    print("player won")
elif player=="scissors" and ai=="paper":
    print("player won")
elif player=="paper" and ai=="rock":
    print("player won")
else:
    print("ai won")
