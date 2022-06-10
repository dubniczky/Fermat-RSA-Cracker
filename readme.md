# Insufficiently Random RSA Cracker

Python script to crack RSA keys generated with insufficiently random prime number generators

## Introduction

A python implementation of RSA key cracking using Fermat's factorization algorithm. The algorithm allows the efficient calculation of the prime factors of a composite number that is a product of two close primes.

Close in our case means at least half the bits of a key are equivalent, which is almost impossible in the case of a sufficiently random number generator. Some libraries however, lacked the sufficient randomness, especially in case of numbers generated in quick succession (time based seed).
