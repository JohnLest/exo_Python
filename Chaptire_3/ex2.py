# Reprendre la suite de Fibonacci (Chap 1 Ex 3) et l'adapter dans une fonction récursive.

def main():
    fibbo(1, 1)

def fibbo(a, b):
    print(a) 
    if (a < 610): # 610 est le 15em chiffre de la suite 
        fibbo(b, a+b) # b va prendre la place de a et b va prendre la valeur de a + b 

if __name__ == "__main__":
    main()