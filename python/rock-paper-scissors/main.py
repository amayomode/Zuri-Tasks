import random

options = ["R", "P", "S"]
codex = {"R": "Rock", "P": "Paper", "S": "Scissors"}


def find_winner(user_input, computer_input):
    winning_combos = ["RS", "PR", "SP"]
    combo = user_input + computer_input
    if combo in winning_combos:
        return (True, "You Win")
    if combo[::-1] in winning_combos:
        return (True, "Computer Wins")

    return (False, "It Is A Tie")


print("Simple Rock Paper Scissors Game \n")
print(
    'Instructions\n------------------\n"R" for "rock" \n"P" for "paper", \n"S" for "scissors"\n------------------\n'
)
while True:
    user_input = input('Pick an option between "R", "P" or "S": ').upper()
    if user_input not in options:
        print("Invalid option")
        continue
    else:
        computer_input = random.choice(options)
        print(f"Player ({codex[user_input]}) : CPU ({codex[computer_input]})")
        is_winner, winner = find_winner(user_input, computer_input)

        if is_winner:
            print(winner)
            print("Game Over")
            break
        else:
            print(winner)
            continue
