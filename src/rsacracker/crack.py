from math import isqrt

class CrackResult():
    d: int
    p: int
    q: int
    phi: int
    steps: int

    def __init__(self, d, p, q, phi, steps) -> None:
        self.d = d
        self.p = p
        self.q = q
        self.phi = phi
        self.steps = steps

    def __str__(self) -> str:
        return f'### d:\n{self.d}\n### p:\n{self.p}\n### q:\n{self.q}\n### phi:\n{self.phi}\n### steps:\n{self.steps}\n'


def crack_rsa(n: int, e: int, *, rounds: int = 100, offset: int = 0) -> CrackResult:
    if n < 1:
        return None
    if e < 2:
        return None
    if rounds < 1:
        return None
    if offset < 0:
        return None

    a = int( isqrt(n) + 1 )
    b = -1
    steps = 0

    for _ in range(offset, offset + rounds + 1):
        b2 = int(a**2 - n)
        if b2 == isqrt(b2) ** 2:
            b = int(isqrt(b2))
            break
        a += 1
        steps += 1

    if b == -1:
        return None

    p = a + b
    q = a - b
    phi = (p-1) * (q-1)
    #print(p, q, phi, a, b)
    d = pow(e, -1, phi)
    return CrackResult(d, p, q, phi, steps)
