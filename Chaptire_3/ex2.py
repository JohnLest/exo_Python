# Reprendre la suite de Fibonacci (Chap 1 Ex 3) et l'adapter dans une fonction récursive.

def main():
    fibo(1, 1)

def fibo(a, b):
    """ Cette fonction affiche les 15 premiers chiffres de la suite de Fibonacci """
    print(a) 
    if (a < 610): # 610 est le 15em chiffre de la suite 
        fibo(b, a+b) # b va prendre la place de a et b va prendre la valeur de a + b 

if __name__ == "__main__":
    main()