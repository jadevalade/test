


import networkx as nx


class Graphe:
    def __init__(self, arcs={}, sommets=set()):
        self.arcs = arcs
        self.sommets = sommets

    def ajouter_sommet(self, sommet):
        if sommet not in self.sommets:
            self.sommets.add(sommet)
            self.arcs.setdefault(sommet)
            self.arcs[sommet] = {}

    def ajouter_arete(self, source, destination, poids):
        self.ajouter_sommet(source)
        self.ajouter_sommet(destination)
        self.arcs[source].setdefault(destination)
        self.arcs[source][destination] = poids

    def afficher_arcs(self):
        for x in self.arcs:
            for y in self.arcs[x].keys():
                print(f"Source : {x}, Destination : {y}, poids : {self.arcs[x][y]}")

    def plus_court_chemin(self, depart, arrivee, memo):
        if memo[depart][arrivee] != None:
            return memo[depart][arrivee]
        if depart == arrivee:
            return (0, [arrivee])
        min_cout = 1000
        min_s = []
        for x in self.arcs[depart].keys():
            print(x)
            cout = self.plus_court_chemin(x, arrivee, memo)[0] + self.arcs[depart][x]
            if min_cout > cout:
                min_cout = cout
                min_s = [depart] + self.plus_court_chemin(x, arrivee, memo)[1]
        memo[depart][arrivee] = (min_cout, min_s)
        return memo[depart][arrivee]


exemple = Graphe()
exemple.ajouter_arete("A", "B", 1)
exemple.ajouter_arete("A", "C", 1)
exemple.ajouter_arete("B", "D", 1)
exemple.ajouter_arete("C", "B", 2)
exemple.ajouter_arete("B", "C", 2)
exemple.afficher_arcs()

memo = dict((sommet, dict((s, None) for s in exemple.sommets)) for sommet in exemple.sommets)

#print(exemple.plus_court_chemin("A", "D", memo))