def askLetter():
    return input("Proposez une lettre ! \n")

def initCurrentWord(word):
    init = []
    for i in range(len(word)):
        init.append('_')
    return init

def printCurrentWord(currentWord):
    string = ''
    for c in currentWord:
        string += c + ' '
    print(string)

def posLetterInWord(word, letter):
    posRes = []
    for i in range(len(word)):
        pos = i
        value = word[i]
        if value.lower() == letter.lower():
            posRes.append(pos)
    return posRes

def playOnce(posPlayed,currentWord,letter):
    for val in posPlayed:
        if val == 0 :
            currentWord[val] = letter.upper()
        else :
            currentWord[val] = letter
    return currentWord

def isWon(data):
    return ''.join(data["currentWord"]) == data["word"]