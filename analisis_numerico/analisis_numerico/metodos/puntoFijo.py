import sympy as sp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def CorregirFuncion(inputString):
    NuevoString = inputString
    if "cos" in inputString:
        NuevoString = NuevoString.replace("cos(", "cos(")
    if "sin" in inputString:
        NuevoString = NuevoString.replace("sin(", "sin(")
    if "tan" in inputString:
        NuevoString = NuevoString.replace("tan(", "tan(")
    if "log" in inputString:
        NuevoString = NuevoString.replace("log(", "log(")
    if "exp" in inputString:
        NuevoString = NuevoString.replace("exp(", "exp(")
    if "^" in inputString:
        NuevoString = NuevoString.replace("^", "**")
    if "abs" in inputString:
        NuevoString = NuevoString.replace("abs(", "Abs(")
    return NuevoString

def pf(x0, Tol, niter, f_str, g_str):
    x = sp.symbols('x')

    # Convertir las cadenas de funciones en funciones simbólicas
    f = sp.sympify(CorregirFuncion(f_str))
    g = sp.sympify(CorregirFuncion(g_str))

    # Inicialización de variables
    c = 0
    fm = [float(f.subs(x, x0))]
    fe = fm[c]
    E = [Tol + 1]
    error = E[c]
    xn = [x0]
    N = [c]

    # Graficar la función f(x)
    x_values = np.linspace(x0 - 1, x0 + 1, 400)
    f_values = [float(f.subs(x, val)) for val in x_values]
    plt.plot(x_values, f_values, label='$f(x)$')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gráfica de la función f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Iteración del método de punto fijo
    while error > Tol and fe != 0 and c < niter:
        xn.append(float(g.subs(x, x0)))
        fm.append(float(f.subs(x, xn[c+1])))
        fe = fm[c+1]
        E.append(abs(xn[c+1] - x0))
        error = E[c+1]
        x0 = xn[c+1]
        N.append(c + 1)
        c += 1

    # Almacenar resultados en un DataFrame de Pandas
    df = pd.DataFrame({
        'n': N,
        'Xn': xn,
        'Fx': fm,
        'Error': E
    })

    # Resultados
    if fe == 0:
        print(f'{x0} es raiz de f(x)')
    elif error < Tol:
        print(f'{x0} es una aproximación de una raiz de f(x) con una tolerancia= {Tol}')
    else:
        print(f'Fracasó en {niter} iteraciones')

    return df