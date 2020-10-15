from random import choice

def getWords(nb):
    liste = ["Bonjour","Hockey","Salut","Helicoptere","Parapluie",'Montre','Arbre',"Voiture","Formule"]
    if (nb < len(liste)):
        return liste[0:nb]
    else :
        return liste

def getWord():
    return choice(getWords(10))

def getMaxTry():
    return 10