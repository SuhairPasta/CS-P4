# a:

class NewRecord:
    def __init__(self, key, item1, item2):
       key = self.key
       item1 = self.item1
       item2 = self.item2
       

# b:i:
# Write program code to declare the global arrays HashTable and Spare
HashTable = [NewRecord]*200
Spare = [NewRecord]*100

# b:ii:
# procedure Initialise() stores an empty record in each element in HashTable and Spare
def Initialise():
    global HashTable, Spare
    HashTable = [NewRecord(-1,-1,-1)] *200
    Spare = [NewRecord(-1,-1,-1)] *100
    
def main():
    print(Initialise())
    
main()
