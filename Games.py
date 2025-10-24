import random
import math

While_True = True

print
age = int(input("What is your age?: "))
age.lower()
if age >= 18:
    while True:
        person = input("Who do you vote for Arsen or kalen? ")
        if person == "arsen":
            print("1 vote has been added for Arsen" )
            break
        elif person == "kalen":
            print("1 vote has been added for Kalen")
            break
        else:
            print("An error occured try again")
else:
    print("You are not old enough to vote yet!")

