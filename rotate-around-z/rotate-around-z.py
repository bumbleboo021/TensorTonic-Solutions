import numpy as np

def rotate_around_z(points, theta):
    """
    Rotate 3D point(s) around the Z-axis by angle theta (radians).
    """
    # Your code here
    x, y = np.cos(theta), np.sin(theta)
    Rz = np.array([[x, -y, 0], [y, x, 0], [0, 0, 1]])
    return (Rz @ np.array(points).T).T
    pass
# Input: points = [[1, 0, 0], [0, 1, 2]], theta = π/2

# Output: [[0, 1, 0], [-1, 0, 2]] (approx)