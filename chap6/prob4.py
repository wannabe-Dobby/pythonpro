import random

print("Welcome to hangman")
print("------------------------------------")

words = ["bear", "deer", "dolphin", "goat", "hamster", "koala", "mouse", "panda", "pony", "raccoon"]

random_word = random.choice(words)

for x in random_word:
      print("_", end = " ")

# wrong 갯수에 따른 hangman 모양
def print_hangman(wrong):
    if (wrong == 0):
        print("\n +--+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif (wrong == 1):
        print("\n +--+")
        print(" O  |")
        print("    |")
        print("    |")
        print("   ===")
    elif (wrong == 2):
        print("\n +--+")
        print(" O  |")
        print(" |  |")
        print("    |")
        print("   ===")
    elif (wrong == 3):
        print("\n +--+")
        print(" O   |")
        print("/|   |")
        print("     |")
        print("   ===")
    elif (wrong == 4):
        print("\n +--+")
        print(" O   |")
        print("/|\  |")
        print("     |")
        print("   ===")
    elif (wrong == 5):
        print("\n +--+")
        print(" O   |")
        print("/|\  |")
        print("/    |")
        print("   ===")
    elif (wrong == 6):
        print("\n +--+")
        print(" O   |")
        print("/|\  |")
        print("/ \  |")
        print("   ===")

# 추측한 문자를 입력했을 때
# 그 문자가 랜덤 단어에 포함되어 있으면 그 자리에 그 문자를 쓰고, 포함되지 않았으면 공백을 남긴다.
def print_word(guessed_letters):
    counter = 0
    right_letters = 0
    for char in random_word:
        if char in guessed_letters:
            print(random_word[counter], end = " ")
            right_letters += 1
        else:
            print(" ", end = " ")
        counter += 1
    return right_letters

# 랜덤 단어의 자릿수 표시 (overline으로)
def print_lines():
    print("\r")
    for char in random_word:
        print("\u203E", end = " ")

# current_guess_index : 전체 배열에서 비교해보는 자리 (한 루프를 돌 때마다 1씩 더해서 다음 루프에서 는 다음 자리를 보도록 함)
# current_letter_guessed : 추륵했던 문자들을 모아놓는 배열
length_of_word_to_guess = len(random_word)
amount_of_times_wrong = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0

while (amount_of_times_wrong != 6 and current_letters_right != length_of_word_to_guess):

    # 문자 추측 받기
    letter_Guessed = input("\nEnter your guess: ")

    # 추측한 문자가 맞았을 때
    if (random_word[current_guess_index] == letter_Guessed):
        print("\nYes", letter_Guessed, "is in the word!")
        print_hangman(amount_of_times_wrong)

        # 단어 출력하기
        current_guess_index += 1
        current_letters_guessed.append(letter_Guessed)
        current_letters_right = print_word(current_letters_guessed)
        print_lines()

    # 추측한 문자가 틀렸을 때
    else:
        print("\n", letter_Guessed, "is not in the word!")

        # 틀린 횟수를 1더해서 hangman 출력하기
        amount_of_times_wrong += 1
        current_letters_guessed.append(letter_Guessed)
        print_hangman(amount_of_times_wrong)

        # 단어 출력하기
        current_letters_right = print_word(current_letters_guessed)
        print_lines()

    print("\nYou've used the following letters:")
    for letter in current_letters_guessed:
        print(letter, end = " ")

print("\n\nGame is over!")
