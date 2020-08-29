import random

WORDLIST = "words.txt"

#function to load file

def loadWords():

    print("Loading word list from file...")
    inFile = open(WORDLIST, 'r')
    line = inFile.readline()
    wordlist = line.split()
    # print("  ", len(wordlist), "words loaded.")
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

def randomD(hiddenword):


    # randomizes the word chosen for game
    index = random.randint(0, len(hiddenword) - 1)

    # assigns radomized word to variable

    displaylist = []
    x = hiddenword[index]
    for _ in range(len(hiddenword)):
        displaylist.append("_")

    for i in range(len(hiddenword)):
        if x == hiddenword[i]:
            displaylist[i] = x


    return ''.join(displaylist)



#main function

def main(hideword):
    print("Welcome to the game, GUESSMAN!")
    print("I am thinking of a word that is", len(hideword), "letters long.")
    global guessedletter
    guessedletter = []
    chancesleft = 0

    # at intial few letter revealed
    w  = randomD(hideword)
    print("here given:",w)
    l = [c for c in w]
    i = 0

    # add already revealed letter to guessedletter
    while i<len(l):
        if(l[i]!='_'):
            guessedletter.append(l[i])
            i = i+1
        i = i+1
    # print(guessedletter)
    # remove guessedletter from availableletters
    g = list(set(guessedletter))
    print("Available letters:", AvailableLetters(g))

    while 10 - chancesleft > 0:
        # print(guessedletter)
        # print(hideword)
        if guessword(hideword,guessedletter):
            print("-------------------")
            print("congratulations,you won")
            break

        else:

            print("*****************")
            print("You have", 10 - chancesleft, "guesses left.")
            g1 = list(set(guessedletter))
            print("Available letters:", AvailableLetters(g1))
            guess=(input("please guess a letter")).lower()

            if guess in guessedletter:
                print("Already guessed that letter",correctwordguessed(hideword,guessedletter))

            elif guess in hideword:
                c = 0
                for i in hideword:
                    if i == guess:
                        c = c + 1
                while c>0:
                    guessedletter.append(guess)
                    c = c - 1
                print("Good guess:",correctwordguessed(hideword,guessedletter))

            else:
                c = 0
                for i in hideword:
                    if i == guess:
                        c = c + 1
                while c > 0:
                    guessedletter.append(guess)
                    c = c - 1
                # guessedletter.append(guess)
                chancesleft += 1
                print("Letter not in hidden word",correctwordguessed(hideword,guessedletter))

        if 10 - chancesleft == 0:
            print("-------------")
            print("Sorry, you ran out of guesses. The word was else.", hideword)
            break

        else:
            continue


hideword = choosedword(wordlist)
main(hideword)







# import random
# def randomD(hiddenword):
#
#
#     # randomizes the word chosen for game
#     index = random.randint(0, len(hiddenword) - 1)
#
#     # assigns radomized word to variable
#
#     displaylist = []
#     x = hiddenword[index]
#     for _ in range(len(hiddenword)):
#         displaylist.append("_")
#
#     for i in range(len(hiddenword)):
#         if x == hiddenword[i]:
#             displaylist[i] = x
#
#
#     print(''.join(displaylist))
#
# randomD("hello")


