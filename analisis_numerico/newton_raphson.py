import numpy as np
import sympy as sp

def newton_raphson(f_str, x0, tol, max_iter):
    x = sp.symbols('x')
    f = sp.sympify(f_str)
    f_prime = sp.diff(f, x)
    
    f_lambda = sp.lambdify(x, f)
    f_prime_lambda = sp.lambdify(x, f_prime)
    
    results = []
    for i in range(max_iter):
        f_x0 = f_lambda(x0)
        f_prime_x0 = f_prime_lambda(x0)
        
        if f_prime_x0 == 0:
            raise ValueError("La derivada es cero en x = {}. El método falla.".format(x0))
        
        x1 = x0 - f_x0 / f_prime_x0
        results.append((i + 1, x0, f_x0, f_prime_x0, x1))
        
        if abs(x1 - x0) < tol:
            break
        
        x0 = x1
    
    return results, f, f_prime