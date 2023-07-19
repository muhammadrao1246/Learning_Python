# FUNCTIONS ARE THE REUSABLE CODE CONTAINERS THAT CAN BE CALLED FROM ANY 
# SEQUENCE OF THE PROGRAM TO EXECUTE FOR A CERTAIN PURPOSE EITHER TO PERFORM A REPITITIVE PROCESS 
# OR SOME CALCULATION OR OPERATION Which code CAN BE SO BIG TO BE ADDED TO THE CURRENT WORKING SECTION


# function with fix number of parameters
def add(val1, val2):
    return val1 + val2

## providing arguments in order as they are parameterized in function definition
print("ADD Function:", 5, "+", 10, "=", add(5, 10))
## can also pass the arguments with named parameters where we don't have to follow order
print("ADD Function:", 5, "+", 10, "=", add(val2=5, val1=10))

# DEFAULT ARGUMENTS
def print_table(table_number = 5): # if no value will be provided then it will automatically take 5 as argument
    print("\nTABLE OF", table_number)
    for i in range(1, 10):
        print(table_number , "x", i, "=", table_number*i)

# RECURSIVE FUNCTIONS
#  a function which call itself and iterate upon itself until aterminal condition met
def factorial( num ):
    if num is 0:
        return 1
    return num * factorial(num-1)

print("\n Factorial of 4 is", factorial(4))

# ARBITRARY ARGUMENTS
# function that can be used where number of arguments are unknown
# known as arbitrary arguments
# as this function will accept the tuple of arguments in its parameters
def sum( *values ):     # dont mess it with c++ pointers
    total = 0
    for value in values:
        total += value
    return total

# calling function with 0 parameter
print("\nSum of no value:", "=", sum())
# calling function with one parameter
print("Sum of one value:", 10, "=", sum(10))
# calling function with three parameter
print("Sum of three values:", 10, "+", 15, "+", 15, "=", sum(10, 15, 15))


# KEYWORD ARGUMENTS
# provide number of arguments as you wish with key value pairs 
# as the keyword should be uniquely defined 
# these arguments will be passed in the form of dictionary to the 
# function
def person_info( **attributes ): # don't confuse it with c++ double pointers
    for attr in attributes.keys():
        print(attr, ":\t", attributes.get(attr), sep="")

# calling function with fruits
print("\nPerson Details Are:")
person_info(PersonName="Muhammad Bin Zulfiqar", 
            FatherName="Zulfiqar Ali Idris",
            Age=19)


