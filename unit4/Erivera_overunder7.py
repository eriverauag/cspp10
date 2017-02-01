import random
 
# function for rolling 2 dice
# name: roll2dice
# arguments: none
# returns: the sum
def roll2dice():

    # generate a random number from 1 to 6
    # generate another random number from 1 to 6
    # get the sum of the two rolls
    # print the sum
    # return the sum
    dice1= random.randint(1 , 6)
    dice2= random.randint(1 , 6)
    dice_sum = dice1 + dice2
    print("Rolled 2 dice: {} + {}".format(dice1,dice2)) 
    print("Total dice roll: {}".format(dice1 + dice2))
    return dice_sum
# function for getting a user's bet
# name: get_bet
# arguments: bank - current player balance
# returns: the bet
def get_bet(bank):
    # ask the player how much they want to bet
    # if player's bet is more than they have
    #   available in bank, then get new bet
    # if player's bet is valid, then return
    #   the bet
    while True:
        print("You have ${} in your bank account.".format(bank_account))
        bet=int(input("How much would you like to bet?: $"))
        if bet<1:
            print("Your bet must be a postitive interger higher than $0")
        elif bet>100:
            print("You only have $100 to bet, you can't bet anymore!")
        else:
            return bet
# function that finds the range given a dice roll
# name: get_range
# arguments: sum of dice
# returns: the range:
#           "over7" if over 7
#           "under7" if under 7
#           "equal7" if equal to 7
def get_range(dice_sum):
    # if the sum is over 7, return "over7"
    # if the sum is under 7, return "under7"
    # if the sum is 7, return "equal7"
    if dice_sum > 7:
        return("over7")
    elif dice_sum < 7:
        return("under7")
    elif dice_sum == 7:
        return("equal7")
 
# function for getting the user's choice of range
# name: choose_range
# arguments: none
# returns: player's choice of range
#       "over7", "under7", or "equal7"
def choose_range():
    print("If over7, you want to roll 8-12. Winner recieves 1:1 payout")
    print("If under7, you want to roll 2-6. Winner recieves 1:1 payout")
    print("If equal7, you want to roll 7. Winner recieves 4:1 payout")
    choice = input("Choose over7,under7, equal7:")
    return choice
    # present user with choices "over7", "under7",
    #   or "equal7"s
    # return their choice
 
# function for the main game