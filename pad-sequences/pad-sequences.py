import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if max_len is None:
        max_len = 0
        for each in seqs:
            max_len = max(max_len, len(each))
    res = np.full((len(seqs), max_len), pad_value)

    for idx, each in enumerate(seqs):
        clone = each[:max_len]
        res[idx, :len(clone)] = clone
    return res
    pass