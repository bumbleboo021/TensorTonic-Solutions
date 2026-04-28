import math
def binary_focal_loss(predictions, targets, alpha, gamma):
    """
    Compute the mean binary focal loss.
    """
    # Write code here
    totalLoss = 0.0
    for each, target in zip(predictions, targets):
        pt = each if target == 1 else 1 - each
        FL = - alpha * ((1 - pt) ** gamma) * math.log(pt)
        totalLoss += FL
    return totalLoss / len(predictions)