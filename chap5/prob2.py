import random

words = ("difficult", "banana", "apple", "python", "daegu", "catholic", "university")

print("Welcome to Word Jumble!\nUnscremble the letters to make a word.")

word1 = random.choice(words)
word1_list = list(word1)
random.shuffle(word1_list)

print("Jumbled word:")

for i in word1_list:
    print(i, end='')
print("")

guess = input(("Your guess: "))
if guess == word1:
  print("Correct!")
else:
  print("Sorry, that's not correct. The word was:", word1)



#for letter in word1:
#  print(letter)
