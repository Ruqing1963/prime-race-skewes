# Prime Race and Skewes Phenomenon - GitHub Repository

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18134004.svg)](https://doi.org/10.5281/zenodo.18134004)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Paper](https://img.shields.io/badge/paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/XXXX.XXXXX)

## Computational Analysis of Chebyshev's Bias and the Skewes Phenomenon

**A Unified Spectral Framework for Prime Number Oscillations**

This repository contains the complete computational infrastructure for our paper investigating two fundamental phenomena in prime number distribution:
1. **Chebyshev's Bias** - The persistent advantage of primes ≡ 3 (mod 4)
2. **Skewes Number** - The first point where π(x) > Li(x)

### 🔬 Key Findings

- ✅ **Spectral confirmation** of bias driver at γ₁ ≈ 6.0209 Hz (0.03% accuracy)
- ✅ **Energy barrier discovery**: DC offset (1.30) > first harmonic (0.7)
- ✅ **Skewes verification** at x ≈ 1.397 × 10³¹⁶ using 100B zeros
- ✅ **Multi-precision validation**: Float32 ↔ Float64 agreement <0.01%

---

## 📁 Repository Structure

```
prime-race-skewes/
│
├── README.md                          # This file
├── LICENSE                            # MIT License
├── CITATION.cff                       # Citation metadata
├── requirements.txt                   # Python dependencies
├── environment.yml                    # Conda environment (optional)
│
├── paper/                             # Academic paper
│   ├── academic_paper.pdf             # Main paper (preprint/published)
│   ├── academic_paper.tex             # LaTeX source
│   └── figures/                       # All figures (300 DPI)
│       ├── figure_01_resonance.png
│       ├── figure_02_bias_drift.png
│       └── ...
│
├── scripts/                           # Main analysis scripts
│   ├── 01_prime_race_analysis.py      # Bias drift regression
│   ├── 02_resonance_detection.py      # Frequency sweep
│   ├── 03_flip_prediction.py          # Zone predictions
│   ├── 04_zone31_validation.py        # Micro-validation
│   ├── 05_skewes_hunter.py           # Main Skewes computation
│   ├── 06_skewes_verification.py     # Result verification
│   ├── 07_precision_check.py         # Float64 validation
│   └── 08_comparative_viz.py         # Energy barrier visualization
│
├── src/                               # Reusable library code
│   ├── __init__.py
│   ├── primes.py                      # Prime generation utilities
│   ├── resonance.py                   # Resonance analysis tools
│   ├── filtering.py                   # Dual-stage filter
│   ├── explicit_formula.py            # Riemann explicit formula
│   └── visualization.py               # Plotting utilities
│
├── data/                              # Data files (small samples)
│   ├── samples/                       # Sample datasets for testing
│   │   ├── prime_race_sample.csv
│   │   └── zone31_sample.csv
│   └── checkpoints/                   # Pre-computed results
│       ├── skewes_checkpoint.npy      # Skewes sum (16 MB)
│       └── processed_files.txt        # File tracking
│
├── notebooks/                         # Jupyter notebooks
│   ├── 01_Quick_Start.ipynb          # Introduction & examples
│   ├── 02_Resonance_Analysis.ipynb   # Interactive resonance
│   ├── 03_Energy_Barrier.ipynb       # Visual exploration
│   └── 04_Reproduction_Guide.ipynb   # Full reproduction steps
│
├── tests/                             # Unit tests
│   ├── test_primes.py
│   ├── test_resonance.py
│   ├── test_filtering.py
│   └── test_explicit_formula.py
│
├── docs/                              # Documentation
│   ├── METHODOLOGY.md                 # Detailed methods
│   ├── REPRODUCIBILITY.md             # Step-by-step guide
│   ├── FAQ.md                         # Frequently asked questions
│   └── API.md                         # Code API documentation
│
└── results/                           # Archived outputs
    ├── figures/                       # Generated figures
    ├── reports/                       # Text summaries
    └── tables/                        # Data tables (CSV/Excel)
```

---

## 🚀 Quick Start

### Prerequisites

```bash
# Python 3.8 or higher
python --version

# Clone repository
git clone https://github.com/Ruqing1963/prime-race-skewes.git
cd prime-race-skewes
```

### Installation

**Option 1: pip (recommended)**
```bash
pip install -r requirements.txt
```

**Option 2: conda**
```bash
conda env create -f environment.yml
conda activate prime-race
```

### Run Example Analysis

```bash
# 1. Quick resonance detection (2 minutes)
python scripts/02_resonance_detection.py

# 2. Prime race analysis (3 minutes)
python scripts/01_prime_race_analysis.py

# 3. Zone 31 validation (5 minutes)
python scripts/04_zone31_validation.py
```

### Interactive Exploration

```bash
jupyter notebook notebooks/01_Quick_Start.ipynb
```

---

## 📊 Main Scripts

### 1. Prime Race Analysis (`01_prime_race_analysis.py`)

Analyzes Chebyshev's bias up to N = 10⁷.

**Usage:**
```bash
python scripts/01_prime_race_analysis.py --N 10000000 --samples 500
```

**Output:**
- Bias drift analysis chart
- Regression statistics (R², intercept, slope)
- Dual-language report (EN + ZH)

**Runtime:** ~3 minutes

---

### 2. Resonance Detection (`02_resonance_detection.py`)

Performs frequency sweep to detect L-function zero.

**Usage:**
```bash
python scripts/02_resonance_detection.py --freq-range 5.8 6.3 --resolution 200
```

**Output:**
- Resonance spectrum plot
- Peak frequency: 6.02111 Hz
- Comparison with theory (6.02094 Hz)

**Runtime:** ~2 minutes

---

### 3. Skewes Hunter (`05_skewes_hunter.py`)

**⚠️ WARNING:** Requires 800GB Riemann zero database

Main computation using explicit formula with 100 billion zeros.

**Usage:**
```bash
python scripts/05_skewes_hunter.py \
    --data-dir /path/to/ZetaData \
    --center-u 727.951332 \
    --window 0.000002 \
    --resolution 2000
```

**Requirements:**
- Odlyzko-Schönhage zero database (800GB)
- 64GB+ RAM recommended
- 16+ CPU cores for parallel processing
- ~48 hours runtime

**Alternative - Use Checkpoint:**
```bash
# Skip 48-hour computation, verify existing results
python scripts/06_skewes_verification.py \
    --checkpoint data/checkpoints/skewes_checkpoint.npy
```

**Runtime:** 1 minute (verification mode)

---

### 4. Precision Verification (`07_precision_check.py`)

Float64 re-verification of golden window.

**Usage:**
```bash
python scripts/07_precision_check.py \
    --checkpoint data/checkpoints/skewes_checkpoint.npy \
    --window-size 1e-5
```

**Output:**
- Float32 vs Float64 comparison
- Relative error < 0.01%
- Precision validation chart

**Runtime:** ~2 minutes

---

## 🔬 Library API

### Prime Generation

```python
from src.primes import get_primes, sieve_range

# Generate primes up to N
primes = get_primes(10_000_000)

# Sieve in range [start, end]
primes_in_range = sieve_range(1_000_000, 2_000_000)
```

### Resonance Analysis

```python
from src.resonance import differential_spectrum

# Compute resonance spectrum
frequencies, strengths = differential_spectrum(
    primes=primes,
    freq_range=(5.8, 6.3),
    resolution=200,
    zeta=0.1
)
```

### Explicit Formula

```python
from src.explicit_formula import compute_oscillatory_sum

# Evaluate π(x) - Li(x) using zeros
zeros = load_zeros("data/zeros.dat")
u_values = np.linspace(727.951, 727.952, 1000)

result = compute_oscillatory_sum(
    zeros=zeros,
    u_values=u_values,
    precision='float64'
)
```

### Dual-Stage Filtering

```python
from src.filtering import dual_stage_filter

# Clean raw zero data
zeros_raw = np.fromfile("zeros.dat", dtype=np.float64)
zeros_clean = dual_stage_filter(
    zeros_raw,
    min_val=14.1,
    max_val=1e15,
    output_dtype=np.float32
)
```

---

## 📈 Reproducing Paper Results

See [`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md) for detailed instructions.

**Quick reproduction:**

```bash
# Run all analyses (excluding 48-hour Skewes computation)
./scripts/run_all.sh

# Output directory: results/
# - 8 figures (300 DPI PNG)
# - 16 text reports (EN + ZH)
# - 1 Excel file (7 sheets)
```

**Estimated time:** ~20 minutes

---

## 🧪 Testing

```bash
# Run unit tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html

# Quick smoke test
pytest tests/ -k "not slow"
```

---

## 📚 Data Sources

### Riemann Zeta Zeros (Required for Skewes computation)

**Source:** Odlyzko-Schönhage Database  
**URL:** http://www.dtc.umn.edu/~odlyzko/zeta_tables/  
**Size:** 800GB (14,580 files)  
**Format:** Binary Float64  
**License:** Public Domain

**Download instructions:** See [`docs/DATA_DOWNLOAD.md`](docs/DATA_DOWNLOAD.md)

**Note:** Checkpoint file `skewes_checkpoint.npy` (16 MB) is included in this repository, enabling verification without downloading 800GB.

---

## 📖 Citation

If you use this code or data in your research, please cite:

**Paper:**
```bibtex
@article{author2026skewes,
  title={Computational Analysis of Chebyshev's Bias and the Skewes Phenomenon: A Unified Spectral Framework},
  author={Author Name},
  journal={[Journal Name]},
  year={2026},
  volume={XX},
  pages={XXX--XXX},
  doi={XX.XXXX/XXXXXXX}
}
```

**Code/Data:**
```bibtex
@software{author2026code,
  author = {Author Name},
  title = {Prime Race and Skewes Phenomenon - Computational Infrastructure},
  year = {2026},
  publisher = {GitHub},
  url = {https://github.com/Ruqing1963/prime-race-skewes}
}
```

**Dataset:**
```bibtex
@dataset{author2026data,
  author = {Author Name},
  title = {Computational Analysis of Chebyshev's Bias: Complete Dataset},
  year = {2026},
  publisher = {Zenodo},
  doi = {10.5281/zenodo.XXXXXXX}
}
```

---

## 📄 License

**Code:** MIT License (see [LICENSE](LICENSE))  
**Data:** CC BY 4.0  
**Paper:** [Journal's copyright policy]

---

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Areas for contribution:**
- Extended precision (Float128) verification
- Parallel processing optimizations
- Additional visualization tools
- Documentation improvements
- Bug reports and fixes

---

## 🐛 Issues

Found a bug or have a question? Please open an issue:
https://github.com/Ruqing1963/prime-race-skewes/issues

---

## 🙏 Acknowledgments

- **Prof. Andrew Granville** - Foundational work on prime races
- **Odlyzko-Schönhage** - Riemann zero database
- **Rubinstein & Sarnak** - Theoretical framework
- **Bays & Hudson** - Skewes bound improvements
- **Open Source Community** - NumPy, SciPy, Matplotlib

---

## 📧 Contact

**Corresponding Author:** [Your Name]  
**Email:** [Your Email]  
**Institution:** [Your Institution]  
**Personal Website:** [Your Website]

---

## 🔗 Links

- **Paper (arXiv):** https://arxiv.org/abs/XXXX.XXXXX
- **Paper (Journal):** [Link when published]
- **Dataset (Zenodo):** https://doi.org/10.5281/zenodo.XXXXXXX
- **Documentation:** https://username.github.io/prime-race-skewes/
- **Issue Tracker:** https://github.com/Ruqing1963/prime-race-skewes/issues

---

**Last Updated:** 2026-01-02  
**Version:** 1.0.0  
**Status:** Active Development
