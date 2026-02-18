def linear_interpolation(values):
    import numpy as np
    return np.interp(
        range(len(values)),
        [i for i, v in enumerate(values) if v is not None],
        [v for v in values if v is not None]
    ).tolist()