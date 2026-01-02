"""Data filtering utilities"""
import numpy as np

def dual_stage_filter(values, x_values, threshold=50):
    """Dual-stage filtering"""
    valid_mag = np.abs(values) < threshold
    valid_type = np.isfinite(values)
    return valid_mag & valid_type

def remove_outliers(values, sigma=3):
    """Remove statistical outliers"""
    mean, std = np.mean(values), np.std(values)
    return np.abs(values - mean) < sigma * std
