from rsacracker import insecure_prime_pair
from rsacracker import crack_rsa

def crack_difference(N, diff):
    p, q = insecure_prime_pair(N, diff)

    n = p*q
    e = 65537
    d = pow(e, -1, (p-1) * (q-1))

    res = crack_rsa(n, e)
    if res is None:
        return 'unsuccessful', str(res)

    if res.d == d:
        return 'correct', str(res)

    return 'incorrect', str(res)

cor, res = crack_difference(1024, 128)
print( cor )
print( res )

cor, res = crack_difference(2048, 512)
print( cor )
print( res )
