import random
randomnum = (random.randint(0,101))
num = int(input("Guess a number between 1-100: "))
amount= 1
while num >= 1 and num <= 100:
    if num < randomnum:
        print("Higher! Guess again")
        num = int(input("Guess a number between 1-100: "))
        amount = amount + 1 
        
    elif num > randomnum:
     print("Lower! Guess again!")
     num = int(input("Guess a number between 1-100: "))
     amount = amount + 1
    
    
   
    
    
    elif num == randomnum:
        print("Good job you got it")
        print(" It took you {} tries".format(amount))
        break
    