import Epic

# -------------------------------------------------------
# Reads the flavors in the specified file (filename) 
# and returns the flavors in a list.
# -------------------------------------------------------
def readFlavors(filename):
    l = []
    file = open(filename)
    for flavor in file:
        l.append(flavor.strip())
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
    flavs = readFlavors("flavors.txt")
    c = countInStock(flavs)
    print "We have %s of your flavors!" % c
    
main()
            