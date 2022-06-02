from Crypto.Util.number import getPrime
from Crypto.Util.number import isPrime
from Crypto.Util.number import getRandomNBitInteger
from Crypto import Random

def getSimilarPrime(N, p, diff):
    d = getRandomNBitInteger(diff)
    number = (p + d + 1) | 1
    
    while (not isPrime(number, randfunc=Random.get_random_bytes)):
        number = number + 2
        if number >= 1 << N:
            number = (1 << N - 1) | 1
    return number

def insecurePrimePair(N, diff):
    p = getPrime(N)
    q = getSimilarPrime(N, p, diff)
    return (p, q)

if __name__ == '__main__':
    import sys
    args = sys.argv[1:]
    if len(args) < 2:
        print("[BITS] [DIFF] - generates a prime pair of BITS length with at least DIFF number of matching bits")
        exit(1)
    
    p, q = insecurePrimePair( int(args[0]), int(args[1]) )
    print(p)
    print()
    print(q)