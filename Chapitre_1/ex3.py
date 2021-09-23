# La suite de Fibonacci est une suite dont chaque termes est égales au deux derniers (1 1 2 3 5 8 13…). 
# Écrire un script qui affiche les 15 premiers termes de la suite

i = 0 # On initialise i à 0
a = b = 1 # on met a et b à la même valeur : 1

print(a) # On imprime a
print(b) # On imprime b

while (i < 13): # Temps que i est strictement plus petit que 13 (car on a déjà affiché les 2 premiers chiffres de la suite)
    a, b = b, a+b # a va prendre la valeur de b, et b va prendre la valeur de a + b
    print(b) # On imprime b
    i += 1 # On incrémente i de 1
