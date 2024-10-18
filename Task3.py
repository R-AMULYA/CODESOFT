import random

def get_computer():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user():
    choice = input("Choose rock, paper, or scissors: ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice.")
        choice = input("Choose rock, paper, or scissors: ").lower()
    return choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user = get_user()
        computer = get_computer()

        result = determine_winner(user, computer)

        print(f"\nYou chose: {user}")
        print(f"Computer chose: {computer}")

        if result == "tie":
            print("It's a tie")
        elif result == "user":
            print("You win this round")
            user_score += 1
        else:
            print("Computer wins this round")
            computer_score += 1

        print(f"\nScore: You {user_score} - {computer_score} Computer")
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing!")
            break

play_game()
