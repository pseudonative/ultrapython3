from random import randint
player_wins=0
computer_wins=0
winning_score=4
while player_wins< winning_score and computer_wins<winning_score:
# for time in range(3):
    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
    print("Rock...")
    print("Paper...")
    print("Scissors...")

    player=input("Player, make your move: ").lower()
    if player=="quit" or player=="q":
        break
    rand_num=randint(0,2)
    if rand_num==0:
        computer="rock"
    elif rand_num==1:
        computer="paper"
    else:
        computer="scissors"
    print(f"computer plays {computer}")

    if player==computer:
        print("it's a tie")
    elif player=="rock":
        if computer=="scissors":
            print("player wins")
            player_wins+=1
        else:
            print("computer wins")
            computer_wins+=1
    elif player=="paper":
        if computer=="rock":
            print("player wins")
            player_wins+=1
        else:
            print("computer wins")
            computer_wins+=1
    elif player=="scissors":
        if computer=="rock":
            print("computer wins")
            computer_wins+=1
        else:
            print("player wins")  
            player_wins+=1 
    else:
        print("Please enter a valid move")
if player_wins>computer_wins:
    print("Congrats,you won!")
elif player_wins==computer_wins:
    print("Forfit")
else:
    print("Oh no :( The computer won")
# print(f"Final Scores: Player... {player_wins} Computer... {computer_wins}")



