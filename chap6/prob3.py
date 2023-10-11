Geek = {"404" : "culeless", "Uninstalled" : "being fired"}

while True:
    print("\n\tGeek Translator\n")
    print("\t0 - Quit\n\t1 - Look Up a Geek Term\n\t2 - Add a Geek Term\n\t3 - Redefine a Geek Term\n\t4 - Delete a Geek Term")

    choice = input("Choice: ")
    print("\n")

    if choice == '0':
        break

    elif choice == '1':
        choice_term = input("What term do you want me to translate?: ")
        trans_term = Geek[choice_term]
        print(choice_term, "means", trans_term)

    elif choice == '2':
        term = input("What term do you want me to add?: ")
        mean = input("Define: ")
        Geek[term] = mean

    elif choice == '3':
        re_term = input("What term do you want me to redefine?: ")
        re_mean = input("Define: ")
        Geek[re_term] = re_mean

    elif choice == '4':
        del_term = input("What term do you want me to delete?: ")
        del Geek[del_term]

    else:
        print("Please re-enter the number in the range of 0 to 4.\n")
        print("Dictionary contains: ")
        for key, value in Geek.items():
            print(f'{key}: {value}')
