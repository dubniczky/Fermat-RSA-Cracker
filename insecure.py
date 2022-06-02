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