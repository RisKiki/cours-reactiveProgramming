from Config import getWord, getMaxTry
from Utils import askLetter, initCurrentWord, printCurrentWord, posLetterInWord, playOnce, isWon

def init():
    data = {
        "nbTry" : 0,
        "word" : getWord(),
        "currentWord" : []
    }
    data["currentWord"] = initCurrentWord(data["word"])

    return data

def main():
    data = init()
    print(data['word'])
    print("Voici le mot à trouver !")
    printCurrentWord(data["currentWord"])
    while data["nbTry"] < getMaxTry() or not isWon(data):
        print("Nombre d'essaye disponible : ", getMaxTry() - data["nbTry"])
        letter = askLetter()
        pos = posLetterInWord(data["word"],letter)
        data["currentWord"] = playOnce(pos,data["currentWord"],letter)
        data["nbTry"] += 1
        printCurrentWord(data["currentWord"])
    
    if isWon(data):
        print("Bravo à toi !")
    else:
        print("Dommage, tu as perdu.")
    rep = input("Voulez-vous quitter ? (o/n)")
    if rep == 'o':
        quit()
    else:
        main()

if __name__ == "__main__":
    main()
