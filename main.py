"lol"
import math

def isprime(p):
    """renvoie si le nombre p est premier ou non """
    if p<=3:
        return True
    premier=True
    for d in range(2,1+int(math.sqrt(p))):
        if p%d==0:
            premier=False
            break
    return premier

def main():
    "renvoie une liste des nombres premiers de 0 à 99"
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print(n)

if __name__ == "__main__":
    main()
