import random

def play():
    user = input("what do you choose? 'r' for rock, 'p' for paper, 's' for scissor\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'it is a tie'

    if is_win(user, computer):
        return 'you won'

    return 'you lost'

def is_win(player, opponent):
    if (player == "r" and opponent == "s") or \
       (player == "p" and opponent == "r") or \
       (player == "s" and opponent == "p"):
        return True
    return False

def play_game():
    while True:
        print(play())
        play_again = input("Do you want to play again? (y/n): ").lower().strip()

        if play_again != 'y':
            print('Thanks for playing!')
            break

if __name__ == '__main__':
    play_game()