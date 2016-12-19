import random

def get_bet(bank_account): 
    while True:
        bet=int(input("How much would you like to bet?: $"))
        if bet<1:
            print("Your bet must be a postitive interger higher than $0")
        elif bet>100:
            print("You only have $100 to bet, you can't bet anymore!")
        else:
            return bet
    
def roll2dice():
    dice1= random.randint(1 , 6)
    dice2= random.randint(1 , 6)
    dice_sum = dice1 + dice2
    print("Rolled 2 dice: {} + {}".format(dice1,dice2)) 
    print("Total dice roll: {}".format(dice1 + dice2))
    return dice_sum

def first_roll_result(dice_sum):
    if dice_sum == 7 or dice_sum == 11:
            print("You win!")
    elif dice_sum == 2 or dice_sum == 3 or dice_sum == 12:
            print("You lose")
    else:
        return dice_sum
    
def second_roll_result(dice_sum,point_roll):
    if dice_sum == point_roll:
        print("You won!")
    elif dice_sum == 7:
        print("You lose!")
    else:
        print("TRY AGAIN")
    while (roll2dice() != 7 and roll2dice() != point_roll):
        print (roll2dice)
        return(second_roll_result(dice_sum,point))
        

        
def craps():
    bank_account=100
    get_bet(bank_account)
    dice = roll2dice()
    first_result = first_roll_result(dice)
    if first_result == "You won!":
        print("You won!")
    elif first_result == "You lose!":
        print("You lose!")
    else:
        print("Point Roll")
        dice = roll2dice()
        point_roll_result = second_roll_result(dice,first_result)
        return(craps())
        
    
craps()