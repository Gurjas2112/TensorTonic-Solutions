import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    position = np.arange(seq_len)[:, np.newaxis]                     # (seq_len, 1)
    div_term = np.exp(
        np.arange(0, d_model, 2) * (-np.log(base) / d_model)
    )                                                                 # (d_model//2,)

    pe = np.zeros((seq_len, d_model))
    pe[:, 0::2] = np.sin(position * div_term)                         # even indices
    pe[:, 1::2] = np.cos(position * div_term[:pe[:, 1::2].shape[1]])  # odd indices

    return pe