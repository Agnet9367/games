import time
import math
import random

number_of_ships = 5

#for _ in range(5):
    #num = random.randint(1, 25)
    #print(num)

A1 = 0
A2 = 0
A3 = 0
A4 = 0
A5 = 0
B1 = 0
B2 = 0
B3 = 0
B4 = 0
B5 = 0
C1 = 0
C2 = 0
C3 = 0
C4 = 0
C5 = 0
D1 = 0
D2 = 0
D3 = 0
D4 = 0
D5 = 0
E1 = 0
E2 = 0
E3 = 0
E4 = 0
E5 = 0

ships = [1, 2, 3, 4, 5, 6, 7, 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25]
random_ships = random.sample(ships, 5)
print(random_ships)
print("---Welcome to Battle Ships---")
user_input = input(f"A {A1}  {A2}  {A3}  {A4}  {A5}\nB {B1}  {B2}  {B3}  {B4}  {B5}\nC {C1}  {C2}  {C3}  {C4}  {C5}\nD {D1}  {D2}  {D3}  {D4}  {D5}\nE {E1}  {E2}  {E3}  {E4}  {E5}\n  1  2  3  4  5\nChoose the cordinate to shoot at: ")


