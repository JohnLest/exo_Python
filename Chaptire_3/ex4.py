#Écrire une fonction qui nous renvoie l'index d'une liste si on donne ça valeur.
#   Si la liste ne contient pas la valeur, renvoyer -1, 
#   si la liste contient plusieurs fois la même valeur renvoyer tous les index.

def main():
    list = [15, 89, 5, 99, 23, 78, 99, 33, 68, 16]
    print(getIndex(list, 7))
    return

def getIndex(liste, val):
    """ Cette fonction permet de retourner l'index d'une valeur """
    listIndex = [] # On va créer une liste d'index
    for index, _val in enumerate(liste):
        if (_val == val): # Quand la valeur de la liste sera égale à la valeur demandé,
            listIndex.append(index) # on va ajouter l'index à la liste

    if (len(listIndex) > 1): # Si la liste a plus d'un élément,
        return listIndex # On retourne toute la liste
    elif(len(listIndex) == 1): # Si elle ne contient qu'un seul index 
        return listIndex[0] # On ne revoie que cet index
    else : return -1 # Et sinon on retourne -1 

if __name__=="__main__":
    main()