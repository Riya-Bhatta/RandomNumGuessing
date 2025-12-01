import random
target = random.randint(1,100)
while True:
    userChoice=int(input("Guess the target --"))
    if(userChoice ==target):
        print("success: Correct Guess !!")
        break
    elif(userChoice<target):
        print("your number was too small. Take a bigger number")
    else:
        print("your number was too big .Take a small number")
        
        print("Game Over")
