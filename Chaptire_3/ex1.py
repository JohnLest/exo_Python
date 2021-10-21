# Écrire un programme qui permet d'enregistrer une liste d'utilisateur. 
# Pour chaque utilisateur il y aura le nom, l'age et la date de naissance.
#   La date de naissance doit être un tuple d'entiers, 
#   mais s'afficher sous le format 'jj-MMM-aaaa' (01-Jan-1999).
# Créer une fonction qui permet de : 
#   enregistrer un nouvel utilisateur, 
#   parcourir tous les utilisateurs, 
#   récupérer un utilisateur via un ID (utiliser les index).
# Le programme ne se termine qu'une fois que l'utilisateur a appuyé sur 'q'.

def main():
    usersList = createUserList()
    if (usersList == -1): # Si la création de la liste a planté 
        return # on s'arrête là.

    while True : 
        choix = printMenu() # On propose à l'utilisateur une liste de choix 
        if(choix == "1"): 
            newUser = addUser()
            if(newUser != -1): # Si l'enregistrement à fonctionné
                usersList.append() # on l'inclus dans la usersList[]
        elif(choix == "2"):
            parcourList(usersList)
        elif(choix == "3"):
            chooseUser(usersList)
        elif(choix.lower() == "q"):
            break
        else:
            print(f"le choix : {choix} n'est pas reconnu par le système")

def printMenu():
    """ Fonction qui permet à l'utilisateur de choisir une des options """
    menu = """Que voulez vous faire? 
    1 - Ajouter un user à la liste
    2 - Parcourir tous les users
    3 - Récupérer un user via un ID
    q - quitter
    """
    return input(menu)

def mapDate(annee, mois, jour):
    """ Fonction qui permet de transformer ma date tuple en date String """
    try:
        ret = -1 # Par défaut la valeur ret est égal à -1
        _mois = [ # On crée une liste de listes dans laquelle on donne le mois et le nombre de jours max
            ["jan", 31], 
            ["fev", 29], 
            ["mar", 31], 
            ["avr", 30], 
            ["mai", 31], 
            ["jun", 30], 
            ["jui", 31], 
            ["aou", 31], 
            ["sep", 30], 
            ["oct", 31], 
            ["nov", 30], 
            ["dec", 31]]
        if (jour >0 and jour <= _mois[mois-1][1] ): # Si le nombre de jour est conforme au mois,
            ret = (f"{jour}-{_mois[mois-1][0]}-{annee}") # la valeur ret devient la chaine de caractères 
        else : print("Erreur dans les dates")
    except Exception as ex: # On gêre les erreurs dans le mapping
        print(f"{type(ex).__name__} Erreur dans les dates")
    return (ret) # On retrourne la valeur de ret

def createUserList():
    """ Fonction qui permet de créer une liste de users """
    usersListe = []
    print("Bienvenue dans la gestion d'utilisateur.")
    try:
        nbrList = int(input("Combien d'utilisateurs voulez vous inscrire : "))
        for i in range(nbrList): 
            usersListe.append(addUser()) # On ajoute le nouvel utilisateur créé à la liste
    except ValueError: # On gêre si l'utilisateur n'a pas donné un Integer
        print("Merci de donner une valeur numérique non null")
        usersListe = createUserList() # Si c'est le cas on recommence la création de usersListe 
    except Exception as ex : # On gêre les éventuelles autres erreurs
        print(f"{type(ex).__name__} Erreur dans la création de la liste")
        return -1
    return (usersListe) # On retourne la liste des users 

def addUser():
    """ Cette fonction sert à créer un dictionnaire d'utilisateur """
    perso = dict()
    try:
        nom = input("Nom : ")
        age = int(input("Age (numérique): "))
        print("Date de naissance (format numérique aaaa-mm-jj) : ")
        annee = int(input("\tannée : "))
        mois = int(input("\tmois : "))
        jour = int(input("\tjour : "))
        if(mapDate(annee, mois, jour) != -1): # On vérifie que la date donnée est valide
            perso["nom"] = nom
            perso["age"] = age
            perso["date"] = (jour, mois, annee)
        else : # sinon on recommence 
            perso = addUser()
    except ValueError: # On verifie que l'utilisateur a bien donné des Integers quand on lui a demandé
        print("Erreur dans l'attribution des données ")
        perso = addUser()
    except Exception as ex : # On gêre les éventuelles autres erreurs
        print(f"{type(ex).__name__} Erreur dans la création de l'utilisateur")
        return -1
    return (perso)

def parcourList(usrLst):
    """ Cette fonction permet de parcourir la liste de tous les utilisateurs """
    for ind, user  in enumerate(usrLst): # On utilise enumarate pour obtenir l'index qui sert d'ID 
        print(f"Voici les données pour le user ID {ind} : ")
        getUser(user) # On appelle la fonction qui va lire le dictionnaire user 
    return

def chooseUser(usersList):
    """ Cette fonction permet de choir un user à partir de son ID """
    try:
        idUser = int(input("Quel est l'ID de l'utilisateur à sortir? "))
        getUser(usersList[idUser]) # On envoie le dictionnaire choisi par l'utilisateur
    except ValueError: # On gêre si l'utilisateur a bien donné un Integer
        print("Merci de donner un ID valide")
    except IndexError: # On gêre si c'est bien un index valide
        print("Merci de donner un ID valide")
    except Exception as ex: # On gêre les éventuelles autres erreurs
        print(f"{type(ex).__name__} Erreur dans la lecture des donées")
    return

def getUser(user):
    """ Cette fonction lit les données présentes dans le dictionnaire user """
    for clef, val in user.items():
        if(clef == "date"): # Si la clef est une date il faut la mapper pour sortir une chaine de caractères
            val = (mapDate(val[2], val[1], val[0]))
        print(f"\t{clef} : {val}")
    return

if __name__ == "__main__":
    main()