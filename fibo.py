

def aux(a, b):
    if a == 0:
        return 1


def fibo(n):
    return n


def fibo_liste(n):
    if n <= 1:
        return 1
    liste = [0 for i in range(n+1)]
    liste[0] = 0
    liste[1] = 1
    for k in range(2, n+1):
        liste[k] = liste[k-2] + liste[k-1]
    return liste[n]


print(fibo_liste(6))
