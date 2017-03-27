import Epic
import random

# ------------------------------------------------
# selects a random word from a file 
# and returns it
# ------------------------------------------------
def pickWord():
    words = []
    
    # read the file and place each word in our list...
    f = open('hangmanWords.txt')
    for w in f:
        w = w.strip()
        words.append(w)
        
    # select a word at random from our list...
    r = random.randrange(0, len(words))
    
    # return the random word
    return words[r]

# ------------------------------------------------
# displays the current board showing where
# letters have been guessed
# ------------------------------------------------
def displayBoard(board):
    for ch in board:
        print "%s " % ch,
    print
     
# ------------------------------------------------
# asks the user to guess a letter and returns
# that letter
# ------------------------------------------------     
def askUserForLetter():
    l = Epic.userString("Please select a letter:")
    return l
 
# ------------------------------------------------
# given the board, the word, and the chosen letter
# this function checks to see if the letter is
# is in the word and then updates the board
# accordingly, if the letter is in the word
# this returns false, otherwise the user guessed
# wrong and true is returned
# ------------------------------------------------
def updateBoard(board, word, letter):
    # check to see if the letter is in the word
    # if it is not, then missed is true...
    missed = letter not in word

    # check each letter in word to see if it 
    # is the letter the user entered
    # if it is, update the board...
    for i in range(0, len(word)):
        if word[i] == letter:
            board[i] = letter
    
    return missed

# ------------------------------------------------
# returns true if the board no longer has any
# * in it, this means all letters have been 
# guessed
# ------------------------------------------------
def testForGameOver(board):
    return "*" not in board
    
def main():
    
    # pick a random word..
    word = pickWord()
    
    # initialize the board...
    board = []
    for ch in word:
        board.append('*');
        
    # initizlize the game...
    misses = 0
    gameOver = False
    
    # start main game loop...
    while gameOver != True:
        
        # display the board...
        displayBoard(board)
        
        # let the user guess a letter...
        letter = askUserForLetter()
        
        # update the board and the misses count...
        if updateBoard(board, word, letter) == True:
            misses = misses + 1
            print "The word does not contain %s! You have %s misse(s)." % (letter, misses)
            
        gameOver = testForGameOver(board)
    
    # print the end of game message
    print "You did it!"
    print "The word is %s" % word
    print "You had %s wrong guesses." % misses
        
main()
        