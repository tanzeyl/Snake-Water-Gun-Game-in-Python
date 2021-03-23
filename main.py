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
    elif option.lower() == "s" and choice == "water":
        print("You won this round.")
        player_score += 1
    elif option.lower() == "s" and choice == "gun":
        print("You lost this round.")
        comp_score += 1
    elif option.lower() == "w" and choice == "snake":
        print("You lost this round.")
        comp_score += 1
    elif option.lower() == "w" and choice == "water":
        print("Tie")
    elif option.lower() == "w" and choice == "gun":
        print("You won this round.")
        player_score += 1
    elif option.lower() == "g" and choice == "snake":
        print("You won this round.")
        player_score += 1
    elif option.lower() == "g" and choice == "water":
        print("You lost this round.")
        comp_score += 1
    elif option.lower() == "g" and choice == "gun":
        print("Tie")
    else:
        print("Please enter a valid character.")
    if option.lower() == "s" or  option.lower() == "w" or option.lower() == "g":
        i += 1
    else:
        continue

if player_score > comp_score:
    print(f"You won the game with score {player_score} while computer's score was {comp_score}. You had {10 - (player_score + comp_score)} ties.")
elif comp_score > player_score:
    print(f"You lost the game with score {player_score} while computer's score was {comp_score}. You had {10 - (comp_score + player_score)} ties.")
else:
    print(f"This game was a tie with both scores equal to {player_score}.")