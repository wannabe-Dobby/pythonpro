import random

print("I sense your energy. Your true emotions are coming across my screen.\nYou are...")

mood = random.randrange(1, 5)

if mood == 0:
  print("\
         -----------\n\
         |         |\n\
         | O     O |\n\
         |   <     |\n\
         |         |\n\
         | .     . |\n\
         |  `...`  |\n\
         -----------")

elif mood == 1:
  print("\
         -----------\n\
         |         |\n\
         | O     O |\n\
         |   <     |\n\
         |         |\n\
         | ------- |\n\
         |         |\n\
         -----------")

elif mood == 2:
  print("\
         -----------\n\
         |         |\n\
         | O     O |\n\
         |   <     |\n\
         |         |\n\
         |   ...   |\n\
         | .`   `. |\n\
         -----------")
else:
  print("Illegal mood value!")

print("\n...today.")
