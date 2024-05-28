import sympy as sp

def trapecio(a, b, n, func):
    h = abs(b - a) / n  # Calcular el tamaño del paso
    f0 = func(a)  # Valor de la función en el extremo a
    fn = func(b)  # Valor de la función en el extremo b
    suma = f0 + fn  # Inicializar la suma con los valores de los extremos

    for i in range(1, n):  # Bucle para los valores intermedios
        fi = func(a + i * h)
        suma += 2 * fi

    val = suma * h / 2  # Calcular el valor final de la integral
    return val

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
    print(f"Resultado de la integral de {func_input} en el intervalo [{a}, {b}] con {n} puntos: {resultado}")

if __name__ == "__main__":
    main()
