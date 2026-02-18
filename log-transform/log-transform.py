def log_transform(values):
    import numpy as np
    return np.log1p(values).tolist()