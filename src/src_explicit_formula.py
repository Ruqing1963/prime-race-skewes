"""Explicit formula utilities"""
import numpy as np

def compute_pi_minus_li(x, zeros, max_terms=10000):
    """Compute π(x) - Li(x)"""
    log_x = np.log(x)
    result = 0
    for gamma in zeros[:max_terms]:
        result += np.cos(gamma * log_x) / (0.5 + 1j*gamma)
    return -2 * result.real / log_x
