import numpy as np
import matplotlib.pyplot as plt
import io
import urllib, base64

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
    return round(integral, 5)

def funcion_ejemplo(x):
    return x**3

def graficar_funcion(f, a, b, n, result):
    x = np.linspace(a, b, 1000)
    y = f(x)

    plt.figure(figsize=(10, 5))
    plt.plot(x, y, label='f(x)')

    x_sub = np.linspace(a, b, n+1)
    y_sub = f(x_sub)

    for i in range(0, n, 3):
        x_fill = np.linspace(x_sub[i], x_sub[i+3], 100)
        y_fill = f(x_fill)
        plt.fill_between(x_fill, y_fill, alpha=0.3)
    
    # Marcar el punto de la solución en la gráfica
    plt.scatter([b], [f(b)], color='red', zorder=5, label=f'Resultado: {result:.5f}')
    plt.text(b, f(b), f'{result:.5f}', fontsize=12, ha='left', va='bottom')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'Integración por el método de Simpson 3/8\nResultado: {result:.5f}')
    plt.legend()
    plt.grid(True)

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    plt.close()

    return uri
