''' Challenge: Coin Flip

Objective: Use the random module and if/else statements to simulate a 50/50 coin toss.'''

import random

num = random.randint(0, 1)   # Generates a random number that's either 0 or 1

if num > 0.5:
  print('Heads')
else:
  print('Tails')
