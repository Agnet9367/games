import random
import math
import time

print("Hello")
time.sleep(1)
name = input("Whats your name? ")
print(f"Welcome to my game! {name} my name is Void")
time.sleep(3)
print("The Rulles are pretty simple")
time.sleep(1)
print("There is a gun with 6 bullets, random amount of them will be blank, and the rest are real! \nThey can be all real! All fake! ")
time.sleep(8)
print("*Bullets are being loaded*")

time.sleep(0.50)
print("---")
time.sleep(0.50)
print("---")
time.sleep(0.50)
print("---")
time.sleep(0.50)
print("---")
time.sleep(0.50)
print("---")
time.sleep(0.50)
print("---")

x = 6

def check_0_in_6_chance():
    result = random.randint(1, x)
    if result == 1: 
        return True
    else:
        return False
def check_1_in_6_chance():
    result = random.randint(1, x)
    if result == 1: 
        return True
    else:
        return False
def check_2_in_6_chance():
    result = random.randint(1, x)
    if result == 1: 
        return True
    else:
        return False
def check_3_in_6_chance():
    result = random.randint(1, x)
    if result == 1: 
        return True
    else:
        return False
def check_4_in_6_chance():
    result = random.randint(1, x)
    if result == 1: 
        return True
    else:
        return False
def check_5_in_6_chance():
    result = random.randint(1, x)
    if result == 1: 
        return True
    else:
        return False
def check_6_in_6_chance():
    result = random.randint(1, x)
    if result == 1: 
        return True
    else:
        return False
    
user = input(f"Choose who to fire at you({name})? Or me(Void)?:")
time.sleep(3)

chance = random.randint(1, 6)

if chance == 1:
    
elif chance == 2:
    
elif chance == 3:

elif chance == 4:

elif chance == 5:

else:




   



