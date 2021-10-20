# Écrire un programme qui calcule la distance entre deux points (x, y)
# à l'aide d'une fonction lambda.
#   Rappel distance entre 2 points : racine carré de ((x2 - x1)² + (y2 - y1)²) 
#   Rappel racine carré de 1 = 1 exp 0.5


def main():
    vect = lambda pA, pB : ((pB[0]-pA[0])**2 + (pB[1]-pA[1])**2)**0.5 # Fonction lambda qui calcule la distance entre deux points
    print(vect((-2, -1), (6, -3)))
    return
    
if __name__=="__main__":
    main()