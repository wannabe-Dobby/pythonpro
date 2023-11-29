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
        print("mood : ", self.__mood)
        
    def Feed(self, mood_increase):
        print("Yeah!")
        self.setMood(mood_increase)
        print("mood : ", self.__mood)
    
    def Play(self):
        print("Wheee!")
        self.setMood(2)
        print("mood : ", self.__mood)
    
    def setMood(self, level):
        self.__mood += level
        
    def getMood(self):
        self.__mood -= 1

class Food:
    def __init__(self, name, level):
        self.name = name
        self.level = level
    
    def getLevel(self):
        return self.level
    
    def setCriterLevel(self, critter):
        critter.setLevel(self.level)
        
def instruction(food_menu):
    print("\n\tCritter Caretaker\n")
    print("\t0 - Quit")
    print("\t1 - Listen to yout critter")
    print("\t2 - Feed yout critter")
    print("\t3 - Play with yout critter\n")
    
critter_name = input("What do you want to name your critter?: ")
crit = Critter(critter_name, 0)

food_menu = [
    Food("Feed", 5),
    Food("Meat", 3),
    Food("Berry", 1)
]

while True:
    instruction(food_menu)
    num = int(input("Choice: "))
    if num == 0:
        break

    if num == 1:
        crit.Talk()
    
    if num == 2:
        print("Select food:")
        print("1 - Feed")
        print("2 - Meat")
        print("3 - Berry")

        food_choice = int(input("Choose food: "))
        if food_choice == 1:
            crit.Feed(5)
        elif food_choice == 2:
            crit.Feed(3)
        elif food_choice == 3:
            crit.Feed(1)
    
    if num == 3:
        crit.Play()