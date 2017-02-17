from pprint import pprint
dictionary = {}
while True:
    key=input("What key would you like to add?")
    value = input("What value would you like to add? ")
    
    for key in dictionary:
        if input in dictionary:
            print ("Already exists as a value!")
            break
    else:
        dictionary[input]="Does not exist as a value!"
ew = {
    "name:" : "Ethan ",
    "school":"Urban Assembly Gateway",
    "money":10,
    "status":"sad",
    "class":"10th Grade SE"
}

pprint (ew) 