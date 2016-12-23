import random

def get_bet(bank_account): 
    while True:
        print("You have ${} in your bank account.".format(bank_account))
        bet=int(input("How much would you like to bet?: $"))
        if bet<1:
            print("Your bet must be a postitive interger higher than $0")
        elif bet>100:
            print("You only have $100 to bet, you can't bet anymore!")
        else:
            return bet
#User gets asked how much they want to bet and they cannot bet 0 and below or over 100 bucks   
def roll2dice():
    dice1= random.randint(1 , 6)
    dice2= random.randint(1 , 6)
    dice_sum = dice1 + dice2
    print("Rolled 2 dice: {} + {}".format(dice1,dice2)) 
    print("Total dice roll: {}".format(dice1 + dice2))
    return dice_sum
#Computer rolls the dice amd gives you the amount on both dice
def first_roll_result(dice_sum):
    if dice_sum == 7 or dice_sum == 11:
            print("You win!")
            return "You win!"
    elif dice_sum == 2 or dice_sum == 3 or dice_sum == 12:
            print("You lose")
            return "You lose!"
    else:
        return dice_sum
def point_roll_result(point_roll):
    return 1
#This is the result of when the first roll of the dice happens to either get your point number, a win, or a loss    
def second_roll_result(dice_sum,point_roll):
    if dice_sum == point_roll:
        print("You won!")
        
    elif dice_sum == 7:
        print("You lose!")
        
    else:
        while (dice_sum != 7 and dice_sum != point_roll):
            dice_sum=roll2dice()
        return(second_roll_result)
#This is the result of the rest of your rolls, with either you winning off your point number, winning off seven, losing, or moving onto the next roll.


def craps():
    bank_account=100
    get_bet(bank_account)
    dice = roll2dice()
    first_result = first_roll_result(dice)
    if first_result == "You won!":
        print("You won!")
        return(craps())
    elif first_result == "You lose!":
        print("You lose!")
        return(craps())
    else:
        print("Point Roll")
        dice = roll2dice()
        point_roll_result = second_roll_result(dice,first_result)
        return(craps())
        print("___________________________")
        while bank_account > 0:
            if bank_account <= 0:
                return "You have no more moeny in your bank account!"
            elif bank_account > 0:
                return craps()
    
craps()