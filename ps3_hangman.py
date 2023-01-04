#
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, "r")
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def hangman(secretWord):
    """
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    """
    import string

    # Start of the game

    # Cheat for testing print(secretWord)

    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")

    # Convert each different character of the secretWord into a list
    secretWordList = []
    for i in secretWord:
        if not (i in secretWordList):
            secretWordList.append(i)

    # For the progress output, convert all of secretWord into a list
    secretWordListFull = []
    for i in secretWord:
        secretWordListFull.append(i)

    # Initiate list: progress, which will print the progress of the successful and missing character of the secretWord
    progress = []
    for i in range(0, len(secretWord)):
        progress.append("_ ")

    # List for memoization of the already guessed character
    # alreadyGuessed = []

    # Create a list for all alphabet characters
    allLetters = []
    counter = 0
    for i in string.ascii_lowercase:
        allLetters.append(i)
        counter += 1

    guessesLeft = 8
    correctGuess = 0

    while guessesLeft > 0:

        if correctGuess == len(secretWordList):
            break

        print("-------------")
        print("You have", guessesLeft, "guesses left.")
        print("Available letters:", "".join(allLetters))

        letterGuessed = input("Please guess a letter: ")
        letterGuessed = letterGuessed.lower()

        if not (letterGuessed in allLetters):
            print("Oops! You've already guessed that letter:", "".join(progress))
            continue

        elif letterGuessed in secretWord:
            correctGuess += 1
            del allLetters[allLetters.index(letterGuessed)]

            # Update the progress to show the newly completed character in the secretWord
            for _ in range(0, (len(secretWordListFull))):
                if letterGuessed in secretWordListFull:
                    correctIndex = secretWordListFull.index(letterGuessed)
                    progress[correctIndex] = letterGuessed
                    secretWordListFull[correctIndex] = "~"

            print("Good guess:", "".join(progress))

        else:
            guessesLeft -= 1
            del allLetters[allLetters.index(letterGuessed)]
            print("Oops! That letter is not in my word:", "".join(progress))

            # When you've completed your hangman function, uncomment these two lines
            # and run this file to test! (hint: you might want to pick your own
            # secretWord while you're testing)

    print("-----------")
    if correctGuess == len(secretWordList):
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was " + str(secretWord) + ".")


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
