import Epic

# -------------------------------------------------------
# Asks the user to enter five flavors of 
# ice cream and returns the flavors in a list.
# -------------------------------------------------------
def getFlavors():
    l = []
    l.append(Epic.userString("Enter Flavor 1:"))
    l.append(Epic.userString("Enter Flavor 2:"))
    l.append(Epic.userString("Enter Flavor 3:"))
    l.append(Epic.userString("Enter Flavor 4:"))
    l.append(Epic.userString("Enter Flavor 5:"))
    return l    
    
# -------------------------------------------------------
# Counts the number of flavors in the specifie 
# list (flavors) that are in stock.  The shop only 
# has vanilla, chocolate, and stawberry.  
# NOTE: the test should be case insensitive.
# -------------------------------------------------------
def countInStock(flavors):
    count = 0
    for f in flavors:
        if f.upper() == "VANILLA" or f.upper() == "CHOCOLATE" or f.upper() == "STRAWBERRY":
            count = count + 1
    return count
    
def main():
    flavs = getFlavors()
    c = countInStock(flavs)
    print "We have %s of your flavors!" % c
    
main()
            