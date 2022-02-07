import random

rand = random.randint(1,100)

print("Pick an integer between 1 and 100")

val = int(input())

def checkingNumber():
    global val
    if val > rand:
        print("You are too high, Pick a number lower number")
        val = int(input())
    else:
        print("You are too low, Pick a number higher number")
        val = int(input())
        
while val != rand:
    checkingNumber()

if val == rand:
    print("You got the correct answer!")