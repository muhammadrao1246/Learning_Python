# LAMBDA FUNCTIONS ARE CALLED ANONYMOUS FUNCTIONS
# A FUNCTION THAT IS DECLARED LIKE A VARIABLE WITH THE RESERVED WORD 'LAMBDA'
# THAT CAN ACCEPT MANY ARGUMENTS BUT CAN CONTAIN ONLY EXPRESSION WHICH'S RESULT WILL BE RETURNED

# ALL FUNCTIONS PROPERTIES REGARDING PARAMETER TYPES AND RETURN TYPES ARE APPLICABLE TO LAMBDA
# EXCEPT THE BODY SEGMENT WHICH CAN ONLY CONTAIN A SINGLE STATEMENT



# here there are two parameters are defined and but single expression will be returned
adder = lambda a, b : a + b  

# arbitrary example
fruits = lambda *fruits : fruits.__str__()

# making alias of print function
printer = lambda message, sep=" ", end="\n" : print(message, sep=sep, end=end)


printer("\nADDITION OF 5 + 10 = ", end=str(adder(5 , 10)))

printer("\nSUMMER FRUITS: ", end=fruits("apple", "mangoes", "bnanas"))
