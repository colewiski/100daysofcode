
'''
Your life left to live in weeks.

A motivational counter.

Assuming you live to be 90 years old, how many weeks, months, or days do you have left?
'''

daysinayear = 365
weeksinayear = 52
monthsinayear = 12

oldage = 90

currentage = int(input("\nWhat is your current age? "))

daysleft = int((oldage - currentage) * daysinayear)
weeksleft = int((oldage - currentage) * weeksinayear)
monthsleft = int((oldage - currentage) * monthsinayear)
summersleft = int(oldage - currentage)

message = f"\nYou have {daysleft} days left, {weeksleft} weeks left, and {monthsleft} months left to continue aliving.\nThat's only {summersleft} more summers to enjoy, now go out there and enjoy this existence!\n"

print(message)