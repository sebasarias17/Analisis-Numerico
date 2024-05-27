import numpy as np
import sympy as sp

def trapecio(a, b, n, func):
    h = abs(b - a) / n  # Calcular el tamaño del paso
    f0 = func(a)  # Valor de la función en el extremo a
    fn = func(b)  # Valor de la función en el extremo b
    suma = f0 + fn  # Inicializar la suma con los valores de los extremos

    print(f"{'Iteración':<10}{'x':<10}{'f(x)':<15}{'Suma acumulada'}")
    print(f"{'0':<10}{a:<10.1f}{f0:<15.4f}{suma:.4f}")

    for i in range(1, n):  # Bucle para los valores intermedios
        xi = a + i * h
        fi = func(xi)
        suma += 2 * fi
        print(f"{i:<10}{xi:<10.1f}{fi:<15.4f}{suma:.4f}")

    suma_final = suma * h / 2  # Calcular el valor final de la integral
    print(f"{n:<10}{b:<10.1f}{fn:<15.4f}{suma:.4f}")
    print(f"\nSuma final acumulada: {suma_final:.4f}")
    return suma_final

def main():
    # Solicitar los datos al usuario
    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))
    n = int(input("Ingrese el número de puntos n: "))
    
    # Solicitar la función al usuario
    x = sp.symbols('x')
    func_input = input("Ingrese la función a integrar (en términos de x): ")
    func_sympy = sp.sympify(func_input)
    func = sp.lambdify(x, func_sympy, 'numpy')
    
    # Calcular la integral usando el método del trapecio compuesto
    resultado = trapecio(a, b, n, func)
    print(f"\nResultado de la integral de {func_input} en el intervalo [{a}, {b}] con {n} puntos: {resultado:.4f}")

if __name__ == "__main__":
    main()
