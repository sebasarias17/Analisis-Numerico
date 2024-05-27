import numpy as np
import matplotlib.pyplot as plt

def simpson_38(f, a, b, n):
    if n % 3 != 0:
        raise ValueError("El número de subintervalos (n) debe ser múltiplo de 3.")
    
    h = (b - a) / n
    integral = f(a) + f(b)
    
    for i in range(1, n):
        x_i = a + i * h
        if i % 3 == 0:
            integral += 2 * f(x_i)
        else:
            integral += 3 * f(x_i)
    
    integral *= 3 * h / 8
    return integral

def graficar_funcion(f, a, b, n):
    x = np.linspace(a, b, 1000)
    y = f(x)
    
    x_sub = np.linspace(a, b, n+1)
    y_sub = f(x_sub)
    
    plt.plot(x, y, label='f(x)')
    
    for i in range(0, n, 3):
        x_fill = np.linspace(x_sub[i], x_sub[i+3], 100)
        y_fill = f(x_fill)
        plt.fill_between(x_fill, y_fill, alpha=0.3)
    
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Integración por el método de Simpson 3/8')
    plt.legend()
    plt.grid(True)
    plt.show()

def funcion_ejemplo(x):
    return x**3

if __name__ == "__main__":
    a = float(input("Ingrese el límite inferior de integración (a): "))
    b = float(input("Ingrese el límite superior de integración (b): "))
    
    while True:
        n = int(input("Ingrese el número de subintervalos (múltiplo de 3): "))
        if n % 3 == 0:
            break
        print("El número de subintervalos (n) debe ser múltiplo de 3. Inténtelo de nuevo.")
    
    try:
        resultado = simpson_38(funcion_ejemplo, a, b, n)
        print(f"El resultado de la integración es: {resultado}")
        graficar_funcion(funcion_ejemplo, a, b, n)
    except ValueError as e:
        print(e)
