
# GLOBAL VARIABLES ARE THOSE VARAILBLES THAT HAVE GLOBAL SCOPE MEANS 
# THEY CAN BE ACCESSED ANYWHERE IN THE PROGRAM AND CAN BE MANIPULATED

# if want to use global variable here i can declare it like that before using it

global iam_global
 
iam_global = 20 #now this variable can be used throughout the program



# functions in python
def car():
    print("Car plate number", iam_global)


car()