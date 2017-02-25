import Epic

def main():
    keepGoing = True
    while keepGoing:
        msg = Epic.userString("Enter a message (enter exit to quit):")
        if msg == "quit":
            keepGoing = False
        else:
            print msg

main()