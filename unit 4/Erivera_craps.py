import random
def roll2dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print("Rolled 2 dice: {} {}".format(dice1,dice2))
    return dice_sum
def roll_result():
    dice1 + dice2 = roll_result()
    if roll_result() == "7,11": 
        return "Win"
    elif roll_result() == "2,3,12":
        return "Lose"
    else:
        return "Point"
def bet+money(bank_account):
    bet=int(input("How much money do you want to bet?"))
    if bet <0:
        return