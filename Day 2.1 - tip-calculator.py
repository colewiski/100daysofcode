
'''
100 days of Python

Day 2: Tip Calculator
'''

# Welcome to the tip calculator.
# What was the total bill? -
# How many people to split the bill? -
# What percentage tip would you like to give? - - or -
# Each person should pay: $-

# Welcome message
print("\nWelcome to the tip calculator.\nJust enter numbers, no symbols.\n")

# User input data
totalbill = float(input("What was the total bill, including tax? $"))
payers = float(input("How many people shall split the bill? "))
tip = float(input("What percentage tip would you like to give? (1-20)"))

# In case someone selects "0" for no tip, the math won't divide by 0. 
if input == 0:
    tip = float(1)

# Maths for calculation
includingtip = float((totalbill / payers) * ((tip / 100) + 1.0))
notincludingtip = float(totalbill / payers)

finalwithtip = "{:.2f}".format(includingtip)
finalnotip = "{:.2f}".format(notincludingtip)

# Round result to 2 decimal places
print(f"\nEach person should pay ${finalwithtip} including tip, or ${finalnotip} discluding the tip.\n")

print(f"\nEach person should pay ${finalwithtip} including tip, or ${finalnotip} discluding the tip.\n")