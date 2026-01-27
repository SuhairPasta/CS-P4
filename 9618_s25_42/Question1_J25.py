# 1:a:

# TopOfStack is a global variable initialised to –1
TopOfStack = -1
# Stack is a global array of strings with all elements initialised to "-1"
Stack = [-1]*20


# b:

# Push() takes a string parameter and attempts to store it on the stack
def Push(data):
    global Stack, TopOfStack
    # returns –1 if the stack is full
    if TopOfStack >=20:
        return -1
    #  returns 1 if the parameter is successfully pushed onto the stack
    else:
        TopOfStack +=1
        Stack[TopOfStack] = data
        return 1
    

# c:

# Pop() returns the next item from the stack
def Pop():
    global Stack, TopOfStack
    # returns "–1" if the stack is empty
    if TopOfStack == -1:
        return -1
    else:
        returnVal = Stack[TopOfStack]
        TopOfStack -= 1
        return returnVal
    

# d:

def ReadData(fileName):
    global Stack, TopOfStack