'''
Functions for generating deliberately insecure random prime pairs for demonstration purposes.
'''

from Crypto.Util.number import getPrime
from Crypto.Util.number import isPrime
from Crypto.Util.number import getRandomNBitInteger
from Crypto import Random

def get_similar_prime(N, p, diff):
    d = getRandomNBitInteger(diff)
    number = (p + d + 1) | 1

    while not isPrime(number, randfunc=Random.get_random_bytes):
        number = number + 2
        if number >= 1 << N:
            number = (1 << N - 1) | 1
    return number

def insecure_prime_pair(N, diff):
    p = getPrime(N)
    q = get_similar_prime(N, p, diff)
    return (p, q)

if __name__ == '__main__':
    import sys
    args = sys.argv[1:]
    if len(args) < 2:
        print('Generates an insecure prime pair')
        print('[BITS] [DIFF]')
        print('   - BITS: prime bit length')
        print('   - DIFF: maximum difference in last bits')
        sys.exit(1)

    pair = insecure_prime_pair( int(args[0]), int(args[1]) )
    print(pair[0])
    print()
    print(pair[1])
