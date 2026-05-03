import numpy as np

def bootstrap_mean(x, n_bootstrap=1000, ci=0.95, rng=None):
    """
    Estimates the mean of a 1D dataset and its confidence interval using bootstrap resampling.
    
    Returns: (boot_means, lower, upper)
    """

    if rng is None:
        rng = np.random.default_rng()        
    x = np.asarray(x)
    n = len(x)

    bootstrap_samples = rng.choice(x, size=(n_bootstrap, n), replace=True)
    
    boot_means = np.mean(bootstrap_samples, axis=1)
    
    alpha = 1.0 - ci
    lower_quantile_prob = alpha / 2.0
    upper_quantile_prob = 1.0 - (alpha / 2.0)
    
    lower = np.quantile(boot_means, lower_quantile_prob)
    upper = np.quantile(boot_means, upper_quantile_prob)
    
    return boot_means, lower, upper
    pass