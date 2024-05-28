import numpy as np

def divided_differences(x, y):
    n = len(x)
    coef = np.zeros([n, n])
    coef[:,0] = y

    for j in range(1, n):
        for i in range(n - j):
            coef[i, j] = (coef[i + 1, j - 1] - coef[i, j - 1]) / (x[i + j] - x[i])

    return coef[0, :]

def newton_polynomial(coef, x_data, x):
    n = len(coef) - 1
    p = coef[n]
    for k in range(1, n + 1):
        p = coef[n - k] + (x - x_data[n - k]) * p
    return p

def newton_interpolating_polynomial(x, y):
    coef = divided_differences(x, y)
    def poly_func(xi):
        return newton_polynomial(coef, x, xi)
    return poly_func, coef

def polynomial_expression(coef, x_data):
    terms = []
    for i, c in enumerate(coef):
        term = f"{c:.2f}"
        for j in range(i):
            term += f"*(x-{x_data[j]:.2f})"
        terms.append(term)
    return " + ".join(terms)