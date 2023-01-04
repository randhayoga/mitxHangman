import time
start_time = time.time()


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string

    # Create a list for all alphabet characters
    allLetters = []
    counter = 0
    for i in string.ascii_lowercase:
        allLetters.append(i)
        counter += 1

    # Main loops for the characters removal
    for i in lettersGuessed:
        if i in allLetters:
            del(allLetters[allLetters.index(i)])

    return "".join(allLetters)


lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))

print("--- %s seconds ---" % (time.time() - start_time))
