equation = input("Enter an equation")
first_term = equation[0]
operation= equation[1]
second_term = equation[2]
first= int(first_term)
second= int(second_term)
if operation== "+":
    x= first  + second 
if operation == "-":
    x= first - second 
if operation == "*":
    x= first * second 
if operation == "/":
    x= first / second 
if operation == "%":
    x= first % second 
else:
    print ("operation is invalid")
print("Your answer is {}" .format(x))


