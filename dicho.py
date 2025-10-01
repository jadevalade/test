def aux(l1, x, a, b):
    if a == b:
        return l1[a] == x
    else:
        m = (b+a)//2
        if l1[m] == x:
            return True
        if l1[m] >= x:
            return aux(l1, x, a, m-1)
        else:
            return aux(l1, x, m+1, b)


def cherche(liste, x):
    return aux(liste, x, 0, len(liste) - 1)


print(cherche([2, 3, 4, 5, 6, 7], 2))
