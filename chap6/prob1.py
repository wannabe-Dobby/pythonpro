inventory = ["sword", "armor", "shield", "healing potion"]

print("Your items:")
for item in inventory:
  print(item)

print("\nPress the enter key to continue.\nYou have", len(inventory), "items in yout possession.")

if "healing potion" in inventory:
  print("\nPress the enter key to continue.\nYou will live to fight another day.\n")

num = int (input("Enter the index number for an item in inventory: "))
print("At index", num, "is", inventory[num], "\n")

a = int (input("Enter the index number for an item in inventory: "))
b = int (input("Enter the index number for an item in inventory: "))

print("inventory[", a, ":", b, "]\t", inventory[a:b])

print("\nPress the enter key to continue.\nYou find a chest. It contains:")
chest = ["gold", "gems"]
print(chest)

inventory += chest
print("You add the contents contents of the chest to your inventory.\nYour inventory is now:")
print(inventory)

print("\nPress the enter key to continue.\nYou trade your sword for crossbow.\nYour inventory is now:")
inventory[0] = "crossbow"
print(inventory)

print("\nPress the enter key to continue.\nYou use your gold and gems to buy an orb of future telling.\nYour inventory is now:")
inventory[4:6] = ["orb of future telling"]
print(inventory)

print("\nPress the enter key to continue.\nIn a great battle, your shield is desttoyed.\nYour inventory is now:")
del inventory[2]
print(inventory)

print("\nPress the enter key to continue.\nYour crossbow and armor are stolen by thieves.\nYour inventory is now:")
del inventory[:2]
print(inventory)
