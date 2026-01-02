"""Visualization utilities"""
import matplotlib.pyplot as plt

def setup_publication_style():
    """Configure publication style"""
    plt.rcParams.update({
        'font.size': 11,
        'axes.labelsize': 12,
        'figure.figsize': (10, 6),
        'figure.dpi': 100,
        'savefig.dpi': 300,
    })
