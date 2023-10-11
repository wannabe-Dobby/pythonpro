inventory = ["sword", "armor", "shield", "healing potion"]

print("Your items:")
for item in inventory:
  print(item)

input("\nPress the enter key to continue.")
print("You have", len(inventory), "items in yout possession.")

input("\nPress the enter key to continue.")
if "healing potion" in inventory:
  print("You will live to fight another day.\n")

num = int (input("Enter the index number for an item in inventory: "))
print("At index", num, "is", inventory[num], "\n")

a = int (input("Enter the index number to begin a slice: "))
b = int (input("Enter the index number to end the slice: "))

print("inventory[", a, ":", b, "]\t", inventory[a:b])


input("\nPress the enter key to continue.")
print("You find a chest. It contains:")
chest = ["gold", "gems"]
print(chest)

inventory += chest
print("You add the contents contents of the chest to your inventory.\nYour inventory is now:")
print(inventory)

input("\nPress the enter key to continue.")
print("You trade your sword for crossbow.\nYour inventory is now:")
inventory[0] = "crossbow"
print(inventory)

input("\nPress the enter key to continue.")
print("You use your gold and gems to buy an orb of future telling.\nYour inventory is now:")
inventory[4:6] = ["orb of future telling"]
print(inventory)

input("\nPress the enter key to continue.")
print("In a great battle, your shield is destroyed.\nYour inventory is now:")
del inventory[2]
print(inventory)

input("\nPress the enter key to continue.")
print("Your crossbow and armor are stolen by thieves.\nYour inventory is now:")
del inventory[:2]
print(inventory)
