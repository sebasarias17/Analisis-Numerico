import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def secante(f_str, X0, X1, tolerancia):
    # Definir la función a partir de la cadena de texto
    f = lambda x: eval(f_str)

    n = 0
    error = 1

    resultados = []

    while error > tolerancia:
        n += 1
        Xn1 = X1 - ((f(X1) * (X1 - X0)) / (f(X1) - f(X0)))
        error = abs(Xn1 - X1)
        resultados.append([n, Xn1, f(Xn1), error])
        X0 = X1
        X1 = Xn1

    df_resultados = pd.DataFrame(resultados, columns=['Iteración', 'Xn', 'f(Xn)', 'Error'])
    print(df_resultados)
    return df_resultados

def graficar_funcion(f, raiz):
    # Crear un rango de valores de x para graficar la función
    x = np.linspace(raiz - 5, raiz + 5, 400)
    y = f(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='f(x)')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(raiz, color='red', linestyle='--', label=f'Raíz aproximada: {raiz:.6f}')
    plt.scatter([raiz], [f(raiz)], color='red')  # Punto raíz aproximada
    plt.title('Método de la Secante')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Ejemplo de uso
"""f_str = 'np.exp(-x) - x'
X0 = 0
X1 = 1
tolerancia = 1e-5

df_resultados = secante(f_str, X0, X1, tolerancia)
print(df_resultados)"""
