import numpy as np
import matplotlib.pyplot as plt
import io
import urllib, base64
from typing import Callable, Union

def simpson13(a: Union[int, float], b: Union[int, float], n: int, f: Callable[[Union[int, float]], float]) -> float:
    if n < 2:
        raise ValueError("El número de subintervalos (n) debe ser mayor a 1.")
    
    if n % 2 != 0:
        n += 1  # Ajustar n para que sea par
    
    h = (b - a) / n
    
    x = np.linspace(a, b, n + 1)
    fx = np.array([f(xi) for xi in x])
    
    sum_odd = np.sum(fx[1:-1:2])
    sum_even = np.sum(fx[2:-1:2])
    
    val = (fx[0] + 4 * sum_odd + 2 * sum_even + fx[-1]) * h / 3
    
    return round(val, 5)

def plot_function_and_points(a: float, b: float, f: Callable[[float], float], x: np.ndarray, fx: np.ndarray):
    x_continuous = np.linspace(a, b, 400)
    f_continuous = np.array([f(xi) for xi in x_continuous])

    plt.figure(figsize=(10, 6))
    plt.plot(x_continuous, f_continuous, label='f(x)', color='blue')
    plt.scatter(x, fx, color='red', zorder=5, label='Puntos de integración')
    
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Integración por el método de Simpson 1/3')
    plt.legend()
    plt.grid(True)
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    plt.close()

    return uri

def funcion_a_integrar(x: Union[int, float]) -> float:
    return 1.5 * x**2 + 4 * x + 3500
