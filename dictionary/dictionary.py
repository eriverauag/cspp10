from pprint import pprint
#from the pprint module,import the pprint function
#dictionaries

#dictionaires
d={
# key : value
    "name":"Chen",
    "birthmonth":"August",
    "grade":16
}

#pprint(d)
#print(d['name']) will allow you to only use the name
schedule = {
    "A":"SE11",
    "F":"SE12",
    "G":"SE10",
    "D":"SE12"
}

schedule["E"]="Trig"
print(schedule['E'])
#only checks if it exsit inas a KEY not a value
if "E" in schedule:
    print("E is in the schedule")
else:
    print("E is not in schedule")
        
#how to check if a value exist
for key in schedule:
    if (schedule[key]) == "Trig":
        print("Exist as value!")
        break
else:#this only happen if for loop dosn't break
    print("Does not exist as value!")
long = {
    "name:" : "Mr.Chen ",
    "school":"Urban Assembly Gateway",
    "money":0,
    "status":"tired",
    "class":"10th Grade SE"
}
pprint (long)