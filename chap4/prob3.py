print("\tWelcome to 'Guess My Number'!\n\n\
I'm thinking of a number between 1 and 100.\n\
Try to guess it in as few attempts as possible.\n")

import random

Num = random.randrange(1, 100)

cnt = 0
x = 0

while x != Num:

  cnt += 1
  x = int(input("Take a guess: "))

  if x > Num:
    print("Lower...")
  elif x < Num:
    print("Upper...")
  else:
    print("You guessed it! The number was", Num)
    print("And it only took you", cnt, "tries!")
