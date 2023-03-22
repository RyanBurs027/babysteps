import random

def play():

    user = input("rock paper scissors game! \nPlease only input 'rock, paper, scissors':\n")
    computer = random.choice(['rock', 'paper', 'scissors'])
    computer_picks = f"Computer picks: {computer}"
    player_picks = f"Player picks: {user}"

    
    print(player_picks)
    print(computer_picks)


    if user == computer:
        return "Tie"
    if is_win(user,computer):
        print(f"{user} beats {computer}! You won the game!")
    if is_lost(user, computer):
        print(f"{computer} beats {user},You lost the game! sorry!")
    else:
        print("You need to type 'rock, paper, scissors' only!")
        return play()


def is_win(player,computer):
    if(player == "rock" and computer == "scissors") or \
            (player == "paper" and computer =="rock") or (player == "scissors" and computer == "paper"):
        return True

def is_lost(player,computer):
    if (player == "paper" and computer == "scissors") or \
            (player == "rock" and computer == "paper") or (player == "scissors" and computer == "rock"):
        return True

print(play())