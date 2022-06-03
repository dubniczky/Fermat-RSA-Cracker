from rsacracker import insecure_prime_pair
from crack import crack_rsa

def crack_difference(N, diff):
    p, q = insecure_prime_pair(N, diff)
    print('Generated')

    n = p*q
    e = 65537
    d = pow(e, -1, (p-1) * (q-1))

    res = crack_rsa(n, e, 1000000)
    if res == None:
        return 'unsuccessful', res
    elif res[0] == d:
        return 'correct', res
    else:
        return 'incorrect', res

print( crack_difference(1024, 128) )
