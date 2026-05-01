import numpy as np

def positional_encoding(seq_len, d_model, base = 10000):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    pe = np.zeros((seq_len, d_model))

    pos = np.arange(seq_len)[:, np.newaxis]
    div = np.power(base, np.arange(0, d_model, 2) / d_model)

    pe[:, ::2] = np.sin(pos / div)
    pe[:, 1::2] = np.cos(pos / div[: d_model // 2])
    return pe
    pass