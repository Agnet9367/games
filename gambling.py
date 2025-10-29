import random; import time; import math

coins = 10

print("---Gambling---")
user_input = input(f"What game do you want to play you have {coins} coins!\n\nslot machine\n")
if user_input == "slot machine":
    while True:
        user_input_slot = input(f"type 'start' to spin the slot for 1 coin, you have {coins} coins! ")
        if user_input_slot == "start" and coins > 0:
            coins -= 1
            slots = ["$", "%", "#"]


            slot1 = random.choice(slots);slot2 = random.choice(slots);slot3 = random.choice(slots)
            for i in range(25):
                slot1fake = random.choice(slots);slot2fake = random.choice(slots);slot3fake = random.choice(slots)
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", slot1fake, slot2fake, slot3fake );time.sleep(0.1)
            for i in range(25):
                slot1fake = random.choice(slots);slot2fake = random.choice(slots);slot3fake = random.choice(slots)
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", slot1, slot2fake, slot3fake);time.sleep(0.1)
            for i in range(25):
                slot1fake = random.choice(slots);slot2fake = random.choice(slots);slot3fake = random.choice(slots)
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", slot1, slot2, slot3fake);time.sleep(0.1)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", slot1, slot2, slot3)
            if slot1 == slot2 == slot3:
                print("You won 3 coins!"); coins += 3
            elif slot1 == slot2 or slot1 == slot3 or slot2 == slot3:
                print("You won 2 coins!"); coins += 2
            else:
                print("You didn't win!")
        else:
            print("You don't have enough coins!")

else:
    print("Error")