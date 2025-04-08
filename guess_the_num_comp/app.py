import random


def guess(x):
  random_num = random.randint(1, x)
  guessed = 0

  while random_num != guessed:
    guessed = int(input(f'Guess the number between 1 and {x}: '))

    if guessed > random_num:
      print('Guess Again, too high')
    elif guessed < random_num:
      print('Guess Again, too low')

  print('You guessed right')

guess(10)