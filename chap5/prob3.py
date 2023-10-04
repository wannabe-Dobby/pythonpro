import random

print("Guess the Word!!!\nIn this game, the program selects a word at random, and the player's objective is to guess the chosen word.\n\n")

words = ("difficult", "banana", "apple", "python", "daegu", "catholic", "university")
word = random.choice(words)

word_list = list(word)
guessed_letters = []
attempts = 6

print("Length of the selected word:", len(word))

while attempts > 0:

    answer = ""
    for letter in word:
        if letter in guessed_letters:
            answer += letter + " "
        else:
            answer += "_ "
    
    if answer.replace(" ", "") == word:
        print("Congratulations! You guessedd the word:", word)
        break

    print("Remaining attempts:", attempts)
    print("Current word:", answer)

    guess = input("Guess a letter: ")

    guessed_letters.append(guess)

    if guess not in word_list:
        attempts -= 1
        print("Incorrect guess.")

if attempts == 0:
    print("You've used up all yout attempts. The correct word was", word, ".")
