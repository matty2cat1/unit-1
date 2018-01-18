#Matt Westelman
#1/18/18
#tip.py - How much do I tip my waiter

price = float(input("How much was your meal? "))
percent = int(input("What % do you want to tip? "))

print("Tip $", round(price*(percent/100), 3))
