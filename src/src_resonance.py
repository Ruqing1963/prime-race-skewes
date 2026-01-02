"""Resonance detection"""
import numpy as np

def compute_amplitude(E_values, x_values, frequency):
    """Compute amplitude at frequency"""
    log_x = np.log10(x_values)
    phase = 2 * np.pi * frequency * log_x
    cos_proj = np.mean(E_values * np.cos(phase))
    sin_proj = np.mean(E_values * np.sin(phase))
    return np.sqrt(cos_proj**2 + sin_proj**2)

def frequency_sweep(E_values, x_values, freq_range):
    """Sweep frequency range"""
    return [compute_amplitude(E_values, x_values, f) for f in freq_range]
