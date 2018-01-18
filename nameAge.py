#Matt Westelman
#1/18/18
#nameAge.py - Counting letters and adding numbers

name = input("What is your first and last name? ")
age = int(input("How old are you? "))
var1, var2 = name.split()
print("Your first name has", len(var1), "letters")
print("Your last name has", len(var2), "letters")
print("You will be", age+1, "next year" )
