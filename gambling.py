import random; import time; import math

dollars = 100
betting_amount = 1
print("---Gambling---")
user_input = input(f"What game do you want to play you have {dollars} dollars!\nslot machine\nroulette\n")
if user_input == "slot machine":
    while True:
        user_input_slot = input(f"Type 'start' to spin the slot for {betting_amount} dollar(s), you have {dollars} dollars!\nType 'change' if you want to change betting amount\nType 'exit' if you want to exit\n")
        if user_input_slot == "start" and dollars > 0:
            dollars -= betting_amount
            slots = ["$", "%", "#"]


            slot1 = random.choice(slots);slot2 = random.choice(slots);slot3 = random.choice(slots)
            for i in range(25):
                slot1fake = random.choice(slots);slot2fake = random.choice(slots);slot3fake = random.choice(slots)
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", "|", slot1fake, "|", slot2fake, "|", slot3fake, "|" );time.sleep(0.1)
            for i in range(25):
                slot1fake = random.choice(slots);slot2fake = random.choice(slots);slot3fake = random.choice(slots)
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", "|", slot1, "|", slot2fake, "|", slot3fake, "|" );time.sleep(0.1)
            for i in range(25):
                slot1fake = random.choice(slots);slot2fake = random.choice(slots);slot3fake = random.choice(slots)
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", "|", slot1, "|", slot2, "|", slot3fake, "|" );time.sleep(0.1)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", "|", slot1, "|", slot2, "|", slot3, "|" "\n")
            if slot1 == slot2 == slot3:
                print("You won your bet amount times 2!"); dollars += betting_amount * 2
            else:
                print("You didn't win!")
        elif user_input_slot == "change":
            wanted_betting_amount = int(input("Type the new betting amount here: "))
            if wanted_betting_amount > dollars:
                print("Error")
            else:        
                betting_amount = wanted_betting_amount
        else:
            print("Error")

elif user_input == "roulette":
    num1 = 1;num2 = 2;num3 = 3;num4 = 4;num5 = 5;num6 = 6;num7 = 7;num8 = 8
    while True:
        user_input_roulette = input(f"Type 'start' to spin the roulette for {betting_amount} dollar(s), you have {dollars} dollars!\nType 'change' if you want to change betting amount\nType 'number' to change the number\nType 'exit' if you want to exit\n")
        if user_input_roulette == "start":
            print(num1,    num2,    num3,"\n\n",num8,         num4,  "<---\n\n",num7,    num6,    num5,)


else:
    print("Error")

