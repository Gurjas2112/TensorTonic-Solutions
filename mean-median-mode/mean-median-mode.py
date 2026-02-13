import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    arr = np.array(x)

    mean = np.mean(arr)
    median = np.median(arr)
    
    freq = Counter(arr)
    mode = max(freq, key=freq.get)
    
    return mean, median, mode