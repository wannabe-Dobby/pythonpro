print("\tHigh Scores Keeper\n\n\t0 - Quit\n\t1 - List Scores\n\t2 - Add a Score\n")

scores = {("Moe", 1000), ("Larry", 1500)}

C = int(input("Choice:"))

while C > 0 and C < 2:

  if C == 0:
    break

  elif C == 1:
    print("\tHigh Scores\n")

    for entry in scores:
      score, name = entry
      print("NAME\tSCORE")
      print(name, "\t",  score)

  elif C == 2:
    name = input("What is the player's name?: ")
    score = input("What score did the player get?: ")

    score["name"] = "score"
