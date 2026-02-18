def differencing(series, order):
    import numpy as np
    return np.diff(series, n=order).tolist()