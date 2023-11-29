class Player:
    def blast(self, enemy):
        print("The player blasts an enemy.\n")
        enemy.die()
    
class Alien:
    def die(self):
        print("The alien grasps and says, 'Oh, this is it. This is the big one.\nYes, it's getting dark now. Tell my 1.6 millon larve that I loved them...'")
        print("Good-bye, cruel universe.")

hero = Player()
invader = Alien()

hero.blast(invader)