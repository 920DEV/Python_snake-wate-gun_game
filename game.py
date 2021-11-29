# Snake, Water and Gun Game
import random           # Random module helps to choose the computer it's option

user_options=["s","w","g"]  # These are the option user have to put in this game.

chance=5       # no. of round a user can play
No_of_chances=0
computer_points=0
player_points=0

while No_of_chances<chance:          # If the" no_of_chances" will exceeds the "chance" the will loop will break.
    Player_input= input("Snake(s), Water(w), Gun(g):")
    computer_input=random.choice(user_options)
    # If the user and computer input the same option then that game will be tie.
    if Player_input==computer_input:
        print("This Round is tied")
        print(f"Player choose:{Player_input} and Computer choose: {computer_input}")
    # when Player choose snake as option:
    elif Player_input=="s":
        if computer_input=="w":
            player_points=player_points+1
            print(f"Player choose:{Player_input} and Computer choose: {computer_input}")
            print("You win this round:-")
        elif computer_input=="g":
            computer_points=computer_points+1
            print(f"Player choose:{Player_input} and Computer choose: {computer_input}")
            print("You Loose this round:!")
    # when player choose gun as option:
    elif Player_input=="g":
        if computer_input=="w":
            computer_points=computer_points+1
            print(f"Player choose:{Player_input} and Computer choose: {computer_input}")
            print("You Lose this round")
        elif computer_input=="s":
            player_points=player_points+1
            print(f"Player choose:{Player_input} and Computer choose: {computer_input}")
            print("you won this round:-")
    # when player choose water as option:
    elif Player_input=="w":
        if computer_input=="s":
            player_points=player_points+1
            print(f"Player choose:{Player_input} and Computer choose: {computer_input}")
            print("You won this round :-")
        elif computer_input=="g":
            computer_points=computer_points+1
            print(f"Player choose:{Player_input} and Computer choose: {computer_input}")
            print("You Loose this round")
    # when player choose put a wrong input
    else:
        print("you  put a wrong input:!")

    No_of_chances=No_of_chances+1
    print(f"{chance-No_of_chances} chances left")

print("Game Over.")
print(f"computer get {computer_points} Points.")
print(f"Player get {player_points} Points.")
if computer_points>player_points:
    print(f"Computer win this game by{computer_points-player_points} points.")
elif player_points>computer_points:
    print(f"Player win this game by {player_points-computer_points} points.")
