print("\tWelcome to 'Guess My Number'!\n\n\
I'm thinking of a number between 1 and 100.\n\
Try to guess it in as few attempts as possible.\n")

import random

Num = random.randrange(1, 100)
value = random.randrange(1, 100)

while value == "Num":

  print("Take a guess : ", value)

  vlaue = random.randrange(1, 100)

  if value > Num:
    print("Lower...")
  elif value < Num:
    print("Upper...")
  else:
    print("You guessed it! The number was 15\nAnd it only took you", cnt, "tries!")

  cnt = cnt + 1
