def detect_drift(reference_counts, production_counts, threshold):
    """
    Compare reference and production distributions to detect data drift.
    """
    # Write code here
    score = 0.0
    ref, prod = [], []
    s1, s2 = sum(reference_counts), sum(production_counts)
    for each in reference_counts:
        ref.append(each / s1)
    for each in production_counts:
        prod.append(each / s2)
    for r, p in zip(ref, prod):
        score +=  1 / 2 * abs(r - p)
    if score <= threshold: detect_drift = False
    else: detect_drift = True
    dic = {}
    dic['score'] = score
    dic['drift_detected'] = detect_drift
    return dic
    pass