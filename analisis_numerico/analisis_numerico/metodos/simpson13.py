import numpy as np
import pandas as pd
from typing import Callable, Union

def simpson13(a: Union[int, float], b: Union[int, float], n: int, f: Callable[[Union[int, float]], float]) -> float:
    """
    Calcula la integral definida en el intervalo [a,b] para la función f,
    por el método del Simpson 1/3 compuesto, con n puntos, con n par.

    Args:
        a (Union[int, float]): Límite inferior del intervalo.
        b (Union[int, float]): Límite superior del intervalo.
        n (int): Número de subdivisiones (se ajustará para ser par si es impar).
        f (Callable[[Union[int, float]], float]): Función a integrar.

    Returns:
        float: Resultado de la integral.
    """
    # Asegurarse de que 'n' es par
    if n % 2 != 0:
        n += 1  # Ajustar n para que sea par
    
    # Calcular el paso
    h = (b - a) / n
    
    # Generar los puntos x
    x = np.linspace(a, b, n + 1)
    fx = np.array([f(xi) for xi in x])  # Aplicar f a cada elemento de x
    
    # Calcular la suma
    sum_odd = np.sum(fx[1:-1:2])  # Suma de los puntos impares
    sum_even = np.sum(fx[2:-1:2]) # Suma de los puntos pares
    
    # Calcular el valor final
    val = (fx[0] + 4 * sum_odd + 2 * sum_even + fx[-1]) * h / 3
    
    # Crear un DataFrame para mostrar los datos como una tabla
    df = pd.DataFrame({
        'x': x,
        'f(x)': fx
    })
    
    # Añadir una fila para las sumas y el resultado final
    additional_rows = pd.DataFrame({'x': ['sum_impar', 'sum_par', 'resultado'], 'f(x)': [sum_odd, sum_even, val]})
    df = pd.concat([df, additional_rows], ignore_index=True)
    
    # Mostrar la tabla
    print(df)
    
    return val

def funcion_a_integrar(x: Union[int, float]) -> float:
    """
    Definición de la función a integrar.
    """
    return 1.5 * x**2 + 4 * x + 3500

if __name__ == "__main__":
    # Instrucciones para el usuario
    print("Este programa calcula la integral definida usando el método de Simpson 1/3 compuesto.")
    print("Por favor, ingrese los siguientes valores:")
    
    # Solicitar al usuario que ingrese los valores
    a = float(input("Ingrese el límite inferior (a): "))
    b = float(input("Ingrese el límite superior (b): "))
    
    # Bucle para asegurar que 'n' sea válido
    while True:
        n = int(input("Ingrese el número de subdivisiones (n, debe ser mayor que 1): "))
        if n > 1:
            break
        print("El número de subdivisiones (n) debe ser mayor que 1. Por favor, intente nuevamente.")
    
    # Calcular la integral
    resultado = simpson13(a, b, n, funcion_a_integrar)
    print("Resultado de la integral:", resultado)
