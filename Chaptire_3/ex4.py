#Écrire une fonction qui nous renvoie l'index d'une liste si on donne ça valeur.
#   Si la liste ne contient pas la valeur, renvoyer -1, 
#   si la liste contient plusieurs fois la même valeur renvoyer tous les index.

def main():
    list = [15, 89, 5, 99, 23, 78, 99, 33, 68, 16]
    print(get_index(list, 7))
    return

def get_index(liste, val):
    """ Cette fonction permet de retourner l'index d'une valeur """
    list_index = [] # On va créer une liste d'index
    for index, _val in enumerate(liste):
        if (_val == val): # Quand la valeur de la liste sera égale à la valeur demandé,
            list_index.append(index) # on va ajouter l'index à la liste

    if (len(list_index) > 1): # Si la liste a plus d'un élément,
        return list_index # On retourne toute la liste
    elif(len(list_index) == 1): # Si elle ne contient qu'un seul index 
        return list_index[0] # On ne revoie que cet index
    else : return -1 # Et sinon on retourne -1 

if __name__=="__main__":
    main()