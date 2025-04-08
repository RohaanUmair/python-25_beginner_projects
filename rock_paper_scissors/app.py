import random

def play():
  user_input = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ")
  computer = random.choice(['r', 'p', 's'])

  if user_input == computer:
    return 'Tie'

  if (user_input == 'r' and computer == 's') or (user_input == 'p' and computer == 'r') or (user_input == 's' and computer == 'p'):
    return 'You Won'
  else:
    return 'You Lose'

print(
  play()
)