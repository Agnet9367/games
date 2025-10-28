import random; import time; import math

coins = 10

print("---Gambling---")
user_input = input(f"What game do you want to play you have {coins} coins!\n\nslot machine\n")
if user_input == "slot machine":
    user_input_slot = input(f"type 'start' to spin the slot for 1 coin, you have {coins} coins! ")
    if user_input_slot == "start":
        slots = ["$", "%", "#"]

        slot1 = random.choice(slots);slot2 = random.choice(slots);slot3 = random.choice(slots)
        for i in range(100):
            slot1fake = random.choice(slots);slot2fake = random.choice(slots);slot3fake = random.choice(slots)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n", slot1fake, slot2fake, slot3fake );time.sleep(0.05)
else:
    print("Error")