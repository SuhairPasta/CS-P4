# a:

NumberItems = 20
DataStored = [] * NumberItems


# b:

def Initialize():
    global DataStored, NumberItems
    DataStored = [0] * NumberItems

    Quantity = int(input("Enter the quantity of items (max {}): ".format(NumberItems)))