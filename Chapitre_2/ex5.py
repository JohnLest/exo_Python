# Écrire un script qui permet à l'utilisateur de valider ou non un choix. Quelle que soit la façon dont
# l'utilisateur écrit la réponse (O / Oui / oui / OUI... -  N / Non / NON... )

choix = input("êtes vous d'accord avec moi? ") # On demande à l'utilisateur si il est d'accord

if (choix.lower() == "o" or choix.lower() == "oui" ): # On met la chaine en minuscule pour ne pas devoir gérer toutes les possibilitées
    print("Heureux que vous soyez d'accord avec moi")
elif(choix.lower() == "n" or choix.lower() == "non"):
    print("Je suis triste pour vous")
else: # On pense bien sur à une condition général.
    print("je n'ai pas compris votre réponse")