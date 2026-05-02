import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    # Write code here
    m, v, grad = np.array(m), np.array(v), np.array(grad)
    newm = beta1 * m + (1 - beta1) * grad
    newv = beta2 * v + (1 - beta2) * np.pow(grad, 2)
    mbi = newm / (1 - beta1 ** t)
    vbi = newv / (1 - beta2 ** t)

    param -= lr * mbi /(np.pow(vbi, 0.5) + eps)
    return (param, newm, newv)
    pass