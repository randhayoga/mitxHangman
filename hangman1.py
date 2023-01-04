import time
start_time = time.time()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # Convert each different character of the secretWord into a list
    secretWordList = []
    for i in secretWord:
        if not(i in secretWordList):
            secretWordList.append(i)

    # List for memoization of the already guessed character
    alreadyGuessed = []

    guessesLeft = 8
    correctGuess = 0

    # Reuse variable i as the counter for the letterGuessed list
    i = 0

    # Initiate the letterGuessed because WHY THE FUCK DID THEY EXPECT US TO RETURN ANYTHING WHEN THE PLAYER FUCKING GAVE UP MID GAME
    letterGuessed = "WTF"

    # The main while loops of the game
    while guessesLeft > 0:
        # If user successfully guessed all of the word then they win
        if correctGuess == len(secretWordList):
            return True
        # But if they gave up and don't use all of their 8 chances (which is nonsense) FUCK WHOEVER MADE THIS SHIT
        elif letterGuessed == "." or len(lettersGuessed) == 0:
            return False

        letterGuessed = lettersGuessed[i]

        # If the guess is an already guessed leter, move to the next character then restart to the begginning of the loops
        if letterGuessed in alreadyGuessed:
            # print("Oops! You've already guessed that letter")
            i += 1
            continue
        elif letterGuessed in secretWord:
            correctGuess += 1
            alreadyGuessed.append(letterGuessed)
        else:
            guessesLeft -= 1
            alreadyGuessed.append(letterGuessed)

        i += 1
        lettersGuessed.append(".")

    return False


print(isWordGuessed('durian', ['h', 'a', 'c',
      'd', 'i', 'm', 'n', 'r', 't', 'u']))

print("--- %s seconds ---" % (time.time() - start_time))
