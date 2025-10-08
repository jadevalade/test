import cProfile
import pstats
import time

### Deux fibo

def fibo_naive(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibo_naive(n-1) + fibo_naive(n-2)


def aux(a, b, k):
    if k == 0:
        return a
    else:
        return aux(a+b, a, k-1)

def fibo(n):
    return aux(1, 0, n-1)


### Deux remplissage

def remplir1():
    l= []
    for i in range(1000):
        l.append(i**2)
    return l

def remplir2():
    l = [i**2 for i in range(1000)]
    return l

### Testons !

if __name__ == "__main___":
    with cProfile.Profile() as profile:
        print(fibo_naive(30))
        print(fibo(30))
    results = pstats.Stats(profile)
    results.sort_stats(pstats.SortKey.TIME)
    results.print_stats()
    