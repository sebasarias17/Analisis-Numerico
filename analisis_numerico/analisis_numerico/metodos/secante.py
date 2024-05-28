import matplotlib.pyplot as plt
import numpy as np

def secante(f_str, X0, X1, tolerancia):
    # Definir la función a partir de la cadena de texto
    f = lambda x: eval(f_str)

    n = 0
    error = 1

    resultado = []
    documento = 'secante.txt'
    with open(documento, 'w') as file:
        header = 'Iteración\tXn\t\tf(Xn)\t\tError\n'
        file.write(header)
        print(header)  # Imprimir el encabezado de la tabla
        resultado.append(header.strip())  # Agregar el encabezado a la lista

        while error > tolerancia:
            n += 1
            Xn1 = X1 - ((f(X1) * (X1 - X0)) / (f(X1) - f(X0)))
            error = abs(Xn1 - X1)
            line = f'{n}\t\t{Xn1:.8f}\t{f(Xn1):.8f}\t{error:.8f}\n'
            file.write(line)
            print(line.strip())  # Imprimir cada línea de la tabla
            resultado.append(line.strip())  # Agregar la línea a la lista
            X0 = X1
            X1 = Xn1

        graficar_funcion(f, X1)
        return X1, resultado

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
