print("\t\t\tTrust Fund Buddy\n\n\
Totals tour monthly spending so that your trust fund doesn't run out\n\
<and you're forced to get a real job>.\n\n\
Please enter the requested, monthly costs. since you're rich, ignore pennies\n\
and use only dollars amounts.\n\n")

car = int(input("Lamborghimi Tune-Ups: "))
rent = int(input("Mantattan Apartment: "))
jet = int(input("Private Jet Rental: "))
gifts = int(input("Gifts: "))
food = int(input("Dinning out: "))
staff = int(input("Staff (butlers, chef, driver, assistant): "))
guru = int(input("Personal Guru and coach: "))
games = int(input("Computer Games: "))

total = car + rent + jet + gifts + food + staff + guru + games

print("\nGrand Total :",total)
