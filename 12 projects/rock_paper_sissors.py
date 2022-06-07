import random
def play():
    user = input("Enter (r) for rock, (p) for paper and (s) for sissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return("TIEE!!")

    if is_win(user, computer):
        return("You win.")
    return("You Lost.")

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True
print(play())