
def separe(l1):
    """
    """
    n = len(l1) // 2
    return (l1[:n], l1[n:])


def fusion(l1, l2):
    if l1 == []:
        return l2
    if l2 == []:
        return l1
    print(l1)
    if l1 is not None:
        l1x = l1.pop()
    if l2 is not None:
        l2x = l2.pop()
    if l1x > l2x:
        return [l1x] + fusion(l1, [l2x] + l2)
    else:
        return [l2x] + fusion([l1x] + l1, l2)


def tri_fusion(liste):
    if len(liste) <= 1:
        return liste
    else:
        (l1, l2) = separe(liste)
        fusion(tri_fusion(l1), tri_fusion(l2))


exemple = [2, 1, 3, 2]

print(tri_fusion(exemple))
