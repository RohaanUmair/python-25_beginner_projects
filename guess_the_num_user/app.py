import random

def guess(x):
  print(f'Guess a number between 1 and {x}')
  low = 1
  high = x
  feedback = ''

  while feedback != 'c':
    guessed = random.randint(low, high)
    feedback = input(f'Is {guessed} too high (H), too low (L) or correct (C)? ')

    if feedback.lower() == 'h':
      high = guessed - 1
    elif feedback.lower() == 'l':
      low = guessed + 1

  print(f'The computer guessed your number, {guessed}')

guess(10)