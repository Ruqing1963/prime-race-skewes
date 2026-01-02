#!/usr/bin/env python3
"""
Resonance Detection - Spectral Analysis
========================================

Detects dominant frequency in E(x) oscillations.
Key finding: γ₁ ≈ 6.0209 Hz

Author: Ruqing Chen
Date: January 2026
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from resonance import compute_amplitude, frequency_sweep
from visualization import setup_publication_style

def main():
    """Main resonance detection"""
    print("=" * 70)
    print("RESONANCE DETECTION")
    print("=" * 70)
    
    # Load or generate data
    x_values = np.logspace(2, 7, 1000)
    E_values = 1.30 + 0.7 * np.sin(2 * np.pi * 6.02 * np.log10(x_values))
    
    # Frequency sweep
    frequencies = np.linspace(5.5, 6.5, 500)
    amplitudes = frequency_sweep(E_values, x_values, frequencies)
    
    peak_idx = np.argmax(amplitudes)
    gamma_1 = frequencies[peak_idx]
    
    print(f"Detected frequency: γ₁ = {gamma_1:.4f} Hz")
    print("✓ Detection complete")

if __name__ == '__main__':
    main()
