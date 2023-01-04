import time
start_time = time.time()


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents what letters in secretWord have been guessed so far.
    '''
    # Convert each different character of the secretWord into a list
    secretWordList = []
    for i in secretWord:
        if not(i in secretWordList):
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
            break
        # But if they gave up and don't use all of their 8 chances (which is nonsense) FUCK WHOEVER MADE THIS SHIT
        elif letterGuessed == "." or len(lettersGuessed) == 0:
            break

        letterGuessed = lettersGuessed[i]

        # If the guess is an already guessed leter, move to the next character then restart to the begginning of the loops
        if letterGuessed in alreadyGuessed:
            # print("Oops! You've already guessed that letter:", progress)
            i += 1
            continue
        elif letterGuessed in secretWord:
            correctGuess += 1
            alreadyGuessed.append(letterGuessed)

            # Update the progress to show the newly completed character in the secretWord
            for _ in range(0, (len(secretWordListFull) - 1)):
                if letterGuessed in secretWordListFull:
                    correctIndex = secretWordListFull.index(letterGuessed)
                    progress[correctIndex] = letterGuessed
                    secretWordListFull[correctIndex] = "~"
        else:
            guessesLeft -= 1
            alreadyGuessed.append(letterGuessed)
            # print("".join(progress))

        i += 1
        lettersGuessed.append(".")

    return "".join(progress)
    # print("".join(progress))


print(getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's']))

print("--- %s seconds ---" % (time.time() - start_time))
