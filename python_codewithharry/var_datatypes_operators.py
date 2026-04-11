# # everything thing / data/ function in python is an object.

# a = 1 #numeric
# b = complex(4, 2) #numeric - int
# c = "hello" #text - str
# d = True #boolean 
# e = 2.4553 #numeric - float
# f = [1, 2, 3,[4, 5]] # sequenced - list
# g = (1, 2, 4, 5) #sequenced - tuple
# h = {"name" : "sayema"} #mapped - dict
# print(f"type of a is {type(a)}")
# print(f"type of b is {type(b)}")
# print(f"type of c is {type(c)}")
# print(f"type of d is {type(d)}")
# print(f"type of e is {type(e)}")
# print(f"type of f is {type(f)}")
# print(f"type of g is {type(g)}")
# print(f"type of h is {type(h)}")


'''Operators'''
num1 = int(input("enter a number:"))
num2 = int(input("enter a number:"))
operator = input("enter operator (ex- +,-,/,*,//, %, **) :")

def calculator(num1, num2, operator):
    if operator == "+":
        return (num1 + num2)
    elif operator == "-":
        return(num1 - num2)
    elif operator == "*":
        return(num1*num2)
    elif operator == "/":
        return(num1 / num2)
    elif operator == "//":
        return(num1 // num2)
    elif operator == "%":
        return(num1 % num2)
    elif operator == "**":
        return(num1 ** num2)
    else:
        return("invalid operator")

res = calculator(num1, num2, operator)
print(res)
