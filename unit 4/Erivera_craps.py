import random

def get_bet(bank_account): 
    while True:
        bet=int(input("How much would you like to bet?: $"))
        if bet<0:
            return("Your bet must be a postitive interger higher than $0")
        elif bet>100:
            return("You only have $100 to bet, you can't bet anymore!")
        else:
            return bet
    
    return bet
def roll2dice():
    dice1= random.randint(1,6)
    dice2= random.randint(1,6)
    dice_sum = dice1 + dice2
    print("Rolled 2 dice:{}{}".format(dice1,dice2))
    return dice_sum

def first_roll_result(dice_sum):
    if dice_sum == 7 or dice_sum == 11:
        return("You win!")
    if dice_sum == 2 or dice_sum == 3 or dice_sum == 12:
        return dice_sum
    else:
        return dice_sum
        
