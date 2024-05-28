import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import io
import urllib, base64
from typing import Callable, Tuple

def trapecio(a: float, b: float, n: int, func: Callable[[float], float], func_input: str) -> Tuple[float, str, str]:
    h = abs(b - a) / n
    f0 = func(a)
    fn = func(b)
    suma = f0 + fn

    # Crear la tabla como una cadena HTML
    table_html = "<table><tr><th>Iteración</th><th>x</th><th>f(x)</th><th>Suma acumulada</th></tr>"
    table_html += f"<tr><td>0</td><td>{a:.1f}</td><td>{f0:.4f}</td><td>{suma:.4f}</td></tr>"

    x_values = [a]
    y_values = [f0]

    for i in range(1, n):
        xi = a + i * h
        fi = func(xi)
        suma += 2 * fi
        table_html += f"<tr><td>{i}</td><td>{xi:.1f}</td><td>{fi:.4f}</td><td>{suma:.4f}</td></tr>"
        x_values.append(xi)
        y_values.append(fi)

    suma_final = suma * h / 2
    table_html += f"<tr><td>{n}</td><td>{b:.1f}</td><td>{fn:.4f}</td><td>{suma:.4f}</td></tr>"
    table_html += f"</table><p>Suma final acumulada: {suma_final:.4f}</p>"

    x_values.append(b)
    y_values.append(fn)

    x_range = np.linspace(a, b, 1000)
    y_range = func(x_range)

    plt.figure(figsize=(10, 5))
    plt.plot(x_range, y_range, label=f'Función: {sp.pretty(func_input)}')
    plt.scatter(x_values, y_values, color='red', zorder=5)
    plt.title('Método del Trapecio Compuesto')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)

    plt.axhline(y=suma_final, color='blue', linestyle='--', label=f'Valor de la integral: {suma_final:.4f}')
    plt.legend()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    plt.close()

    return suma_final, table_html, uri

def funcion_ejemplo(x: float) -> float:
    return 1.5 * x**2 + 4 * x + 3500
