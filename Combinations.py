import Epic

def main():
    print "Here are all possible ways I can arrange the numbers 1,2,3"
    r = range(1, 4)
    for a in r:
        for b in r:
            for c in r:
                print "%s%s%s" % (a, b, c)
    
main()