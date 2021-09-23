# La suite de Fibonacci est une suite dont chaque termes est égales au deux derniers (1 1 2 3 5 8 13…). 
# Écrire un script qui affiche les 15 premiers termes de la suite

i = 0
a = b = 1

print(a)
print(b)

while (i < 13):
    a, b = b, a+b
    print(b)
    i += 1
