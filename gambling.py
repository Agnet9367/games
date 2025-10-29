import random; import time; import math

coins = 10
betting_amount = 1
print("---Gambling---")
user_input = input(f"What game do you want to play you have {coins} coins!\nslot machine\n")
if user_input == "slot machine":
    while True:
        user_input_slot = input(f"Type 'start' to spin the slot for {betting_amount} coin, you have {coins} coins!\nType 'change' if you want to change betting amount\nType 'exit' if you want to exit\n")
        if user_input_slot == "start" and coins > 0:
            coins -= betting_amount
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
                print("You won your bet amount times 3!"); coins += betting_amount * 3
            elif slot1 == slot2 or slot1 == slot3 or slot2 == slot3:
                print("You won your bet amount times 2!"); coins += betting_amount *2
            else:
                print("You didn't win!")
        elif user_input_slot == "change":
            wanted_betting_amount = int(input("Type the new betting amount here: "))
            if wanted_betting_amount > coins:
                print("Error")
            else:        
                betting_amount = wanted_betting_amount

else:
    print("Error")