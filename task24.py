# program 1 -Dice roller 
import random 
dice = random.randint(1,6)
print("Dice rolled:",dice)
# program -2 
import random 
coin = random.choice(["Heads","Tails"])
print(coin)
# program -3 
import random 
chars ="abcdefghijklmnopqrstuvwxyz123456789"
password =""
for i in range (6):
    password += random.choice(chars)
print("Password =",password)
# program - 4