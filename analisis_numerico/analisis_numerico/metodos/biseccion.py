import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def biseccion(xi, xs, Tol, niter):
    x = sp.symbols('x')
    f = x**2 - 5*x + 6*sp.sin(x)
    # f = sp.exp(-x-2) - 2*x - 2

    fi = f.subs(x, xi).evalf()
    fs = f.subs(x, xs).evalf()

    with open('resultados.txt', 'w') as file:
        if fi == 0:
            s = xi
            E = [0]
            result = f'{xi} es raíz de f(x)\n'
            print(result)
            file.write(result)
            return s, E, [fi]
        elif fs == 0:
            s = xs
            E = [0]
            result = f'{xs} es raíz de f(x)\n'
            print(result)
            file.write(result)
            return s, E, [fs]
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
            file.write(header)
            row = f'{c:>10} {error:>20.10f} {xa:>20.10f} {xm:>20.10f}\n'
            print(row)
            file.write(row)

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
                file.write(row)

            if fe == 0:
                s = xm
                result = f'{xm} es raíz de f(x)\n'
                print(result)
                file.write(result)
            elif error < Tol:
                s = xm
                result = f'{xm} es una aproximación de una raíz de f(x) con una tolerancia = {Tol}\n'
                print(result)
                file.write(result)
            else:
                s = xm
                result = f'Fracasó en {niter} iteraciones\n'
                print(result)
                file.write(result)

            return s, E, fm
        else:
            result = 'El intervalo es inadecuado\n'
            print(result)
            file.write(result)
            return None, None, None

def plot_function(f, xi, xs):
    x_vals = np.linspace(xi, xs, 1000)
    y_vals = [f.subs(x, val).evalf() for val in x_vals]
    plt.plot(x_vals, y_vals)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gráfico de la función')
    plt.grid(True)
    plt.show()


xi = 1
xs = 3
Tol = 1e-5
niter = 100
s, E, fm = biseccion(xi, xs, Tol, niter)
print(f'Raíz aproximada: {s}')
print(f'Errores: {E}')
print(f'Valores de la función: {fm}')

x = sp.symbols('x')
f = x**2 - 5*x + 6*sp.sin(x)
plot_function(f, xi, xs)