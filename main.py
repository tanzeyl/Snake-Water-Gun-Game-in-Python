import random
print("Welcome to Snake, Water, And Gun.")
lst = ["snake", "water", "gun"]
i = 0
player_score = 0
comp_score = 0
while i < 10:
    choice = random.choice(lst)
    print("Enter your option. Press S for Snake, W for Water, and G for Gun.")
    option = input()
    if option.lower() == "s" and choice == "snake":
        print("Tie")
    if option.lower() == "s" and choice == "water":
        print("You won this round.")
        player_score += 1
    if option.lower() == "s" and choice == "gun":
        print("You lost this round.")
        comp_score += 1
    if option.lower() == "w" and choice == "snake":
        print("You lost this round.")
        comp_score += 1
    if option.lower() == "w" and choice == "water":
        print("Tie")
    if option.lower() == "w" and choice == "gun":
        print("You won this round.")
        player_score += 1
    if option.lower() == "g" and choice == "snake":
        print("You won this round.")
        player_score += 1
    if option.lower() == "g" and choice == "water":
        print("You lost this round.")
        comp_score += 1
    if option.lower() == "g" and choice == "gun":
        print("Tie")
    i += 1

if player_score > comp_score:
    print(f"You won the game with score {player_score} while computer's score was {comp_score}")
elif comp_score > player_score:
    print(f"You lost the game with score {player_score} while computer's score was {comp_score}")
else:
    print(f"This game was a tie with both scores equal to {player_score}.")