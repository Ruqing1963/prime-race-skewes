"""Prime number utilities"""
import numpy as np

def sieve_of_eratosthenes(n):
    """Sieve of Eratosthenes"""
    sieve = np.ones(n//2, dtype=bool)
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = False
    return np.r_[2, 2*np.nonzero(sieve)[0][1::]+1]

def count_primes_by_residue(primes):
    """Count π₁(x) and π₃(x)"""
    pi_1 = np.sum(primes % 4 == 1)
    pi_3 = np.sum(primes % 4 == 3)
    return pi_1, pi_3
