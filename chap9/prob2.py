class Critter:
    """A virtual pet"""
    def __init__(self, name, mood):
        self.name = name
        self.__mood = mood
    
    def Talk(self):
        Critter.getMood(self)

        if self.__mood <= 2:
            mood_word = 'mad'
        elif self.__mood <= 5:
            mood_word = 'soso'
        else:
            mood_word = "happy"

        print("I am", self.name, "and I feel", mood_word, "now")
        print(self.__mood) # del

    def Feed(self, name):
        print("Yeah!")
        Critter.setMood(self, Food.getLevel(self, name))
        print(self.__mood) # del

    def Play(self):
        print("Wheee!")
        Critter.setMood(self, 2)
        print(self.__mood) # del

    def setMood(self, level):
        self.__mood += level
        
    def getMood(self):
        self.__mood -= 1

class Food:
    """Three kinds of food"""
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.__mood = 0
        self.__mood += Food.getLevel(self, name)

    def getLevel(self, name):
        if name == "feed":
            return 5
        if name == "meat":
            return 3
        if name == "berry":
            return 1
        
def instruction():
    print("\n\tCritter Caretaker\n")
    print("\t0 - Quit")
    print("\t1 - Listen to yout critter")
    print("\t2 - Feed yout critter")
    print("\t3 - Play with yout critter\n")

critter_name = input("What do you want to name your critter?: ")
crit = Critter(critter_name, 0)

while True:
    instruction()
    num = int(input("Choice: "))
    if num == 0:
        break

    if num == 1:
        crit.Talk()
    
    if num == 2:
        print("Which food do you want to eat?")
        print("\n\t1 - feed")
        print("\t2 - meat")
        print("\t3 - berry\n")
        eat = int(input())
        
        if eat == 1:
            feed = Food("feed", 5)
            crit.Feed(feed)
        if eat == 2:
            meat = Food("meat", 3)
            crit.Feed(meat)
        if eat == 3:
            berry = Food("berry", 1)
            crit.Feed(berry)

    if num == 3:
        crit.Play()