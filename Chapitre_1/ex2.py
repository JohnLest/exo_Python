# Écrire un scripte qui affiche les 20 premiers termes de la table de multiplication par 7, 
# en signalant au passage (a l’aide d’une astérisque) ceux qui sont des multiples de 3. 
# Exemple : 7 14 *21 28 35 *42 49 ...

i = 1
while (i <= 20):
    if (i%3 == 0):
        print(f"*{i*7}")
    else:
        print(i*7)
    i += 1