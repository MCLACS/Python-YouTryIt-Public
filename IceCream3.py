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
# Counts the number of flavors in the specified 
# list (flavors) that are in stock.  The flavors that
# are in stock should be passed to the funciton as a
# list (instock) and the flavors in this list should
# be in all upper case.
# NOTE: the test should be case insensitive.
# -------------------------------------------------------
def countInStock(instock, flavors):
    count = 0
    for f in flavors:
        if (f.upper() in instock):
            count = count + 1
    return count
    
def main():
    instock = ["VANILLA", "CHOCOLATE", "STRAWBERRY"]
    flavs = readFlavors("flavors.txt")
    c = countInStock(instock, flavs)
    print "We have %s of your flavors!" % c
    
main()
            