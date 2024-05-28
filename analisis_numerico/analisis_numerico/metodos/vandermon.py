import numpy as np

def vandermonde_matrix(x):
    return np.vander(x)

def interpolate_vandermonde(x_values, y_values):
    v_matrix = vandermonde_matrix(x_values)
    coeff = np.linalg.solve(v_matrix, y_values)
    poly = np.poly1d(coeff)
    return poly