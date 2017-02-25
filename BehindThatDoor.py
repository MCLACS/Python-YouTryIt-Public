import random
import time
import Epic

def main():
    # initialize prizes...
    good_prizes = ["New Car!", "$100", "Badge in Python Class", "Free A in Python!"]
    bad_prizes = ["Old Sock", "Smelly Garbage Can", "Sore Throat", "More Homework"]
    
    # create a list for the doors...
    doors = ["", "", ""]

    # place radom bad prizes in behind all three doors...
    random.shuffle(bad_prizes)
    doors[0] = bad_prizes[0]
    doors[1] = bad_prizes[1]
    doors[2] = bad_prizes[2]
    
    # replace a random bad prize with a good one...
    random.shuffle(good_prizes)
    iGoodPrize = random.randrange(0,3)
    doors[iGoodPrize] = good_prizes[0]
    
    # let the user pick a door
    door = Epic.userInt("Pick a door:")
    print "You win..."
    time.sleep(5)
    print "...a %s" % doors[door-1]
    
    
main() #duh