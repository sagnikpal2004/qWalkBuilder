import numpy as np
from scipy.stats import gaussian_kde
from typing import List, Dict, Callable

def calculate_mean(numList: List[float]) -> float:
    return np.mean(numList)

def calculate_std_dev(numList: List[float]) -> float:
    return np.std(numList)

def calculate_variance(numList: List[float]) -> float:
    return np.var(numList)

def calculate_mad(numList: List[float]) -> float:
    mean = calculate_mean(numList)
    return np.mean(np.abs(numList - mean))

def calculate_iqr(numList: List[float]) -> float:
    return np.percentile(numList, 75) - np.percentile(numList, 25)

def calculate_range(numList: List[float]) -> float:
    return np.max(numList) - np.min(numList)

def calculate_cv(numList: List[float]) -> float:
    mean = calculate_mean(numList)
    std_dev = calculate_std_dev(numList)
    return (std_dev / mean) * 100 if mean != 0 else np.inf

def calculate_rms(numList: List[float]) -> float:
    return np.sqrt(np.mean(numList**2))

def calculate_histogram_entropy(numList: List[float], bins: int = 10) -> float:
    hist, bin_edges = np.histogram(numList, bins=bins, density=True)
    prob_density = hist * np.diff(bin_edges)
    prob_density = prob_density[prob_density > 0]
    return -np.sum(prob_density * np.log(prob_density))

def calculate_kde_entropy(numList: List[float], bandwidth: str = 'scott') -> float:
    kde = gaussian_kde(numList, bw_method=bandwidth)
    kde_values = kde.evaluate(numList)
    return -np.mean(np.log(kde_values))

def calculate_total_variation(numList: List[float]) -> float:
    return np.sum(np.abs(np.diff(numList)))

def calculate_normalized_entropy(numList: List[float]) -> float:
    total = np.sum(numList)
    if total == 0:
        return 0.0
    probabilities = numList / total
    probabilities = probabilities[probabilities > 0]  # Filter out zero probabilities
    return -np.sum(probabilities * np.log(probabilities))

fluctuation_measures: Dict[str, Callable[[List[int]], float]] = {
    'Mean': calculate_mean,
    'Standard Deviation': calculate_std_dev,
    'Variance': calculate_variance,
    'MAD': calculate_mad,
    'IQR': calculate_iqr,
    'Range': calculate_range,
    'CV': calculate_cv,
    'RMS': calculate_rms,
    'Histogram Entropy': calculate_histogram_entropy,
    'KDE Entropy': calculate_kde_entropy,
    'Total Variation': calculate_total_variation,
    'Normalized Entropy': calculate_normalized_entropy
}

def calculate_fluctuation_measures(numList: list[float]) -> float:
    results = {}
    for name, func in fluctuation_measures.items():
        results[name] = func(numList)
    return results