import shelve
import random

print("\t\t\tWelcome to Trivia challenge!\n")

quiz = shelve.open("Question.dat")
quiz["0"] = ["On the Run With a Mammal", "Let's say you turn state's evidence and need to \"get on the lamb.\" If you wait/too long, what will happen?",
           "1 - You'll end up on the sheep", "2 - You'll end up on the cow", "3 - You'll end up on the goat", "4 - You'll end up on the emu", 1]
quiz["1"] = ["Math", "12 X 68 = ?", "1 - 786", "2 - 806", "3 - 816", "4 - 846", 3]
quiz["2"] = ["Science", "What is the shape of the earth?", "1 - Circle", "2 - Triangle", "3 - Rectangle", "4 - Pentagon", 1]
quiz["3"] = ["common sense", "How many teeth does a person have in general?", "1 - 20", "2 - 28", "3 - 30", "4 - 32", 2]
quiz["4"] = ["Geography", "Which country does Shibuya belong to?", "1 - Korea", "2 - Japan", "3 - China", "4 - Hong Kong", 2]
quiz.sync()


r = random.choice(list(quiz.keys()))
list = quiz[r]


for item in list[:-1]:
    element = item.split(',')
    print(*element)
    print("\n")

num = int(input("What's your answer?:"))

if num == list[-1]:
    print("맞았습니다!")
else:
    print("틀렸습니다.")