import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def biseccion(f, xi, xs, Tol, niter):
    x = sp.symbols('x')

    fi = f.subs(x, xi).evalf()
    fs = f.subs(x, xs).evalf()

    resultados = []

    if fi == 0:
        s = xi
        E = [0]
        result = f'{xi} es raíz de f(x)\n'
        print(result)
        return pd.DataFrame([(0, xi, 0)], columns=['Iteración', 'xa', 'Error'])
    elif fs == 0:
        s = xs
        E = [0]
        result = f'{xs} es raíz de f(x)\n'
        print(result)
        return pd.DataFrame([(0, xs, 0)], columns=['Iteración', 'xa', 'Error'])
    elif fs * fi < 0:
        c = 0
        xm = (xi + xs) / 2
        fm = [f.subs(x, xm).evalf()]
        fe = fm[c]
        E = [Tol + 1]
        error = E[c]
        xa = xi

        header = f'{"Iteración":>10} {"Error":>20} {"xa":>20} {"xm":>20}\n'
        print(header)
        row = f'{c:>10} {error:>20.10f} {xa:>20.10f} {xm:>20.10f}\n'
        print(row)
        resultados.append([c, xa, xm, error])

        while error > Tol and fe != 0 and c < niter:
            if fi * fe < 0:
                xs = xm
                fs = f.subs(x, xs).evalf()
            else:
                xi = xm
                fi = f.subs(x, xi).evalf()

            xa = xm
            xm = (xi + xs) / 2
            fm.append(f.subs(x, xm).evalf())
            fe = fm[c + 1]
            E.append(abs(xm - xa))
            error = E[c + 1]
            c += 1

            row = f'{c:>10} {error:>20.10f} {xa:>20.10f} {xm:>20.10f}\n'
            print(row)
            resultados.append([c, xa, xm, error])

        if fe == 0:
            s = xm
            result = f'{xm} es raíz de f(x)\n'
            print(result)
        elif error < Tol:
            s = xm
            result = f'{xm} es una aproximación de una raíz de f(x) con una tolerancia = {Tol}\n'
            print(result)
        else:
            s = xm
            result = f'Fracasó en {niter} iteraciones\n'
            print(result)

        df_resultados = pd.DataFrame(resultados, columns=['Iteración', 'xa', 'xm', 'Error'])
        return df_resultados
    else:
        result = 'El intervalo es inadecuado\n'
        print(result)
        return pd.DataFrame(columns=['Iteración', 'xa', 'xm', 'Error'])

