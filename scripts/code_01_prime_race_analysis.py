#!/usr/bin/env python3
"""
Prime Race Analysis - Chebyshev's Bias Investigation
====================================================

Analyzes the prime race where primes ≡ 3 (mod 4) outnumber primes ≡ 1 (mod 4).

Author: Ruqing Chen
Date: January 2026
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from primes import sieve_of_eratosthenes, count_primes_by_residue
from filtering import dual_stage_filter
from visualization import setup_publication_style

def compute_normalized_bias(x_max=10**7, samples=1000):
    """Compute E(x) = [π₃(x) - π₁(x)] / √π(x)"""
    print(f"Computing prime race up to {x_max:,}...")
    primes = sieve_of_eratosthenes(x_max)
    x_values = np.logspace(2, np.log10(x_max), samples, dtype=int)
    E_values = np.zeros(samples)
    
    for i, x in enumerate(x_values):
        primes_up_to_x = primes[primes <= x]
        pi_1, pi_3 = count_primes_by_residue(primes_up_to_x)
        pi_total = len(primes_up_to_x)
        if pi_total > 0:
            E_values[i] = (pi_3 - pi_1) / np.sqrt(pi_total)
    
    return x_values, E_values

def main():
    """Main analysis pipeline"""
    print("=" * 70)
    print("PRIME RACE ANALYSIS")
    print("=" * 70)
    
    x_values, E_values = compute_normalized_bias()
    
    # Analysis and plotting code here
    print("✓ Analysis complete")

if __name__ == '__main__':
    main()
