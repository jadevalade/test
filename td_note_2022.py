import time

def mesure_temps_fonction(fct, N=100):
    begin = time.perf_counter()
    for i in range(N) :
        fct()
    return (time.perf_counter() - begin) / N
    