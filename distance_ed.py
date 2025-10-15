

def est_suite(u, v):
    i = 0
    for x in v:
        if x == u[i]:
            i += 1
    return i

def distance(u, v):
    print(u, v)
    print(len(u), len(v))
    if len(u) ==0:
        return len(v)
    if len(v) ==0 :
        return len(u)
    k = 1
    if u[len(u) -1] == v[len(v) -1]:
        k = 1
    return min(
        distance(u, v[:(len(v) -1)]) +1,
        distance(u[:(len(u) -1)]), v +1,
        distance(u[:(len(u) -1)], v[:(len(v) -1)]) +k
    )

print(distance("cha", "chi"))