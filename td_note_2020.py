from math import *
from numpy import random
import matplotlib.pyplot as plt

random.seed(42)

def distance_table(x1, y1, x2, y2):
    return sqrt( (x1 - x2)**2 + (y1 - y2)**2)


def distance_bord(x1, y1, R):
    return R - distance_table(x1, y1, 0, 0)

def table_alea(R):
    x = R - random.random()*2*R
    y = R - random.random()*2*R
    if distance_bord(x, y, R)>= 0: 
        return (x, y)
    else :
        return table_alea(R)

def ntable_alea(N,R):
    liste_table = []
    for i in range(N) :
        liste_table.append(table_alea(R))
    return liste_table

def table_proches(x1, y1, R, list_table, skip_i):
    minimum = R +1
    ind = 0
    for i in range(len(list_table)):
        if i != skip_i :
            dist = distance_table(x1, y1, list_table[i][0], list_table[i][1])
            if minimum > dist : 
                minimum = dist
                ind = i
    dist = distance_bord(x1, y1, R)
    if dist < minimum:
        return (-1, dist)
    else :
        return (ind, minimum)

def distance_table_alea(N, R):
    liste = ntable_alea(N,R)
    minimum = R + 1
    for i in range(R):
        minimum = min(minimum, table_proches(liste[i][0], liste[i][1], R, liste, i)[1])
    return (liste, minimum)


def meilleur_table_alea(k, N, R):
    liste_liste = []
    for i in range(k):
        liste_liste.append(distance_table_alea(N,R))
    maxi = liste_liste[0]
    for i in range(k):
        if maxi[1] < liste_liste[i][1]:
            maxi = liste_liste[i]
    return maxi


def plot_tables(R, list_tables):
    fig, ax = plt.subplots()
    circle = plt.Circle((0, 0), R, color='blue', fill=False)
    ax.add_artist(circle)
    ax.set_aspect('equal')

    ax.set_xlim([-R, R])
    ax.set_ylim([-R, R])

    test = (ntable_alea(5, 3))
    x = [u[0] for u in list_tables]
    y = [u[1] for u in list_tables]

    plt.scatter(x,y)
    plt.savefig('salle.png', bbox_inches='tight', dpi=300)


plot_tables(1, meilleur_table_alea(100, 3, 1)[0])

