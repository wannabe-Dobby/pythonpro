inventory = ("sword", "armor", "shield", "healing potion")

print("Your items:")
for item in inventory:
  print(item)

input("\nPress the enter key to continue.")
print("You have", len(inventory), "items in your possession.")

input("\nPress the enter key to continue.")
if "healing potion" in inventory:
    print("You will live to fight another day\n")

num = int(input("Enter the index number for an item in inventory: "))
print("At index", num, "is", inventory[num], "\n")

a = int(input("Enter the index number to begin a slice: "))
b = int(input("Enter the index number to end the slice: "))
print("inventory[", a, ":", b, "]\t", inventory[a:b])


input("\nPress the enter key to continue.")
print("You find a chest. It contains:")
chest = ("gold", "gems")
print(chest)

inventory += chest
print("You add the contents of the chest to your inventory.\nYour inventory is now:")
print (inventory)
