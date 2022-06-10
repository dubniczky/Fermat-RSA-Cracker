# Insufficiently Random RSA Cracker

Python script to crack RSA keys generated with insufficiently random prime number generators

## Introduction

A python implementation of RSA key cracking using Fermat's factorization algorithm. The algorithm allows the efficient calculation of the prime factors of a composite number that is a product of two close primes.

Close in our case means at least half the bits of a key are equivalent, which is almost impossible in the case of a sufficiently random number generator. Some libraries however, lacked the sufficient randomness, especially in case of numbers generated in quick succession (time based seed).

## Algorithm

The algorithm is based on the representation of an odd integer as de difference of two squares:

$`N=a^2-b^2`$

Which can be algebraically refactored to:

$`N=(a+b)(a-b)`$

If neither factor equals one, then we can conclude that this is a proper factorization of $`N`$

In this case, if $`N=cd`$ is a factorization of $`N`$, then:

$`N=(\frac{c+d}{2})^2-(\frac{c-d}{2})^2`$

Because $`N`$ is odd, it means $`c`$ and $`d`$ are also going to be odd.

## License

Added general MIT license ([details](/LICENSE))
