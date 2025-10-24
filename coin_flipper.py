import random
flip = input("To flip a coin enter f: \n")
head_tails = random.randint(1, 2)
if head_tails == 1:
    print("You got heads")
else:
    print("You got tails")
