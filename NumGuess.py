import random
import Epic

def main():
    numGuesses = 0
    ans = random.randrange(1, 11)
    keepGoing = True
    while keepGoing:
        guess = Epic.userInt("Enter a guess from 1 to 10:")
        numGuesses = numGuesses + 1
        if guess == ans:
            print "You win! It took %s guesses." % numGuesses
            keepGoing = False
        else:
            if (guess > ans):
                print "You guessed too high!"
            else:
                print "You guessed too low!"
                
            
main()