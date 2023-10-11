scores = {"meo" : 1000, "Larry" : 1500}

while True:
    print("\n\tHigh Scores Keeper\n\n0 - Quit\n1 - List Scores\n2 - Add a Scores\n")
    choice = input("Choice: ")

    if choice == '0':
        break

    elif choice == '1':
        sorted_scores = sorted(scores.items(), key = lambda x : x[1], reverse = True)
        print("\nHigh Scores")
        print("\nNAME\tSCORE")
        for name, score in sorted_scores:
            print(f"{name}\t{score}")

    elif choice == '2':
        print("\n")
        name = input("What is the player's name?: ")
        score = int(input("What score did the player get?: "))
        scores[name] = score

    else:
        print("\nPlease re-enter the number in the range of 0 to 2.")
