from math import isqrt

def crackRSA(n, e, limit):
    a = int(isqrt(n) + 1)
    b = -1
    steps = 0

    for i in range(limit):
        b2 = int(a**2 - n)
        if b2 == isqrt(b2) ** 2:
            b = int(isqrt(b2))
            steps = i
            break
        a += 1

    if (b == -1):
        return None
    
    p = a + b
    q = a - b
    phi = (p-1) * (q-1)
    #print(p, q, phi, a, b)
    d = pow(e, -1, phi)
    return (d, p, q, phi, steps)