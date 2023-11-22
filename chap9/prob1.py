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

    def Feed(self):
        print("Yeah!")
        Critter.setMood(self, 3)
    
    def Play(self):
        print("Wheee!")
        Critter.setMood(self, 2)
    

    def setMood(self, level):
        self.__mood += level
        
    def getMood(self):
        self.__mood -= 1


def instruction():
    print("\n\tCritter Caretaker\n")
    print("\t0 - Quit")
    print("\t1 - Listen to yout critter")
    print("\t2 - Feed yout critter")
    print("\t3 - Play with yout critter\n")

critter_name = input("What do you want to name yout critter?: ")
crit = Critter(critter_name, 0)

while True:
    instruction()
    num = int(input("Choice: "))
    if num == 0:
        break

    if num == 1:
        crit.Talk()
    
    if num == 2:
        crit.Feed()
    
    if num == 3:
        crit.Play()