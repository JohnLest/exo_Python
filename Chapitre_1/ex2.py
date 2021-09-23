# Écrire un scripte qui affiche les 20 premiers termes de la table de multiplication par 7, 
# en signalant au passage (a l’aide d’une astérisque) ceux qui sont des multiples de 3. 
# Exemple : 7 14 *21 28 35 *42 49 ...

i = 1 # On initialise i à 1
while (i <= 20): # Temps que i est plus petit ou égale à 20
    if (i%3 == 0): # Si le reste de la division de i par 3 est de 0, 
        print(f"*{i*7}") # on imprime l'asterisque avant le résultat de l'opération
    else: # Sinon 
        print(i*7) # on imprime juste le résultat de l'opération
    i += 1 # On incrémente i de 1