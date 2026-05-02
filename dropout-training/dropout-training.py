import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """

    x = np.asarray(x)
    if rng:
        cln = rng.random(x.shape)
    else:
        cln = np.random.random(x.shape)
    # Write code here
    dropout_pattern = (cln >= p).astype(float) / (1.0 - p)

    output = (dropout_pattern * x)

    return (output, dropout_pattern)
    pass