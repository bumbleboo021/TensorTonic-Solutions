import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    """
    # Write code here
    N = np.sum(C)
    rowSum = np.sum(C, axis = 0, keepdims = True)
    colSum = np.sum(C, axis = 1, keepdims = True)

    E = rowSum * colSum / N
    chi2 = np.sum((C - E) ** 2 / E)
    return chi2, E
    pass