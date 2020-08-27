import random

WORDLIST = "words.txt"

#function to load file

def loadWords():

    print("Loading word list from file...")
    inFile = open(WORDLIST, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

#function to return a random word

def choosedword(wordlist):
    return random.choice(wordlist)

wordlist = loadWords()

# final output wheather u won or lose
def guessword(hideword,guessedletter):
    c = 0
    for word in guessedletter:
        if word in hideword:
            c += 1
    if c == len(hideword):
        return True
    else:
        return False

def correctwordguessed(hideword,guessedletter):
        s = []
        for i in hideword:
            if i in guessedletter:
                s.append(i)
        ans = ''
        for i in hideword:
            if i in s:
                ans += i
            else:
                ans += '_ '
        return ans

def AvailableLetters(gussedletter):
    import string
    ans=list(string.ascii_lowercase)
    for i in gussedletter:
        ans.remove(i)
    return ''.join(ans)


#main function

def main(hideword):
    print("Welcome to the game, GUESSMAN!")
    print("I am thinking of a word that is", len(hideword), "letters long.")
    global guessedletter
    guessedletter = []
    chancesleft = 0


    while 10 - chancesleft > 0:

        if guessword(hideword,guessedletter):
            print("-------------------")
            print("congratulations,you won")
            break

        else:
            print("*****************")
            print("You have", 10 - chancesleft, "guesses left.")
            print("Available letters:", AvailableLetters(guessedletter))
            guess=(input("please guess a letter")).lower()

            if guess in guessedletter:
                print("Already guessed that letter",correctwordguessed(hideword,guessedletter))

            elif guess in hideword and guess not in guessedletter:
                guessedletter.append(guess)
                print("Good guess:",correctwordguessed(hideword,guessedletter))

            else:
                guessedletter.append(guess)
                chancesleft += 1
                print("Letter not in hidden word",correctwordguessed(hideword,guessedletter))

        if 8 - chancesleft == 0:
            print("-------------")
            print("Sorry, you ran out of guesses. The word was else.", hideword)
            break

        else:
            continue


hideword = choosedword(wordlist)
main(hideword)







