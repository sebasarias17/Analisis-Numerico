import pandas as pd
import numpy as np
from math import *
from analisis_numerico.metodos.inputFixed import CorregirFuncion


def regla_falsa(f, a, b, tol, niter):
    """
    Método de regla falsa
    :param f: funcion a evalua
    :param a: límite inferior
    :param b: límite superior
    :param tol: tolerancia
    :param n: número máximo de iteraciones
    :return: solución
    """
    f = CorregirFuncion(f)
    solucion = 0
    resultados = []
    Error = 100
    x = a
    fa = eval(f)
    x = b
    fb = eval(f)
    if fa == 0:
        solucion = a
        mensaje = f"{solucion} es raiz de f(x)"
        return None, mensaje, solucion
    elif fb == 0:
        solucion = b
        mensaje = f"{solucion} es raiz de f(x)"
        return resultados, mensaje, solucion
    elif fa * fb < 0:
        c = 0
        x = (a * fb - b * fa) / (fb - fa)
        fx = eval(f)
        resultados.append(
            [
                c,
                "{:.5f}".format(a),
                "{:.5f}".format(x),
                "{:.5f}".format(b),
                "{:.3e}".format(fx),
                100,
            ]
        )
        while Error > tol and fx != 0 and c < niter:
            if fx * fa < 0:
                b = x
                fb = fx
            else:
                a = x
                fa = fx
            xTemp = x
            x = (a * fb - b * fa) / (fb - fa)
            fx = eval(f)
            Error = abs(x - xTemp)
            c = c + 1
            resultados.append(
                [
                    c,
                    "{:.5f}".format(a),
                    "{:.5f}".format(x),
                    "{:.5f}".format(b),
                    "{:.3e}".format(fx),
                    "{:.3e}".format(Error),
                ]
            )
        print(resultados)    
        if fx == 0:
            solucion = "{:.5f}".format(x)
            mensaje = str(solucion) + " es raiz de f(x)"
            return resultados, mensaje, solucion
        elif Error <= tol:
            solucion = "{:.5f}".format(x)
            mensaje = (
                str(solucion)
                + " es una aproximacion de un raiz de f(x) con una tolerancia "
                + str(tol)
            )
            return resultados, mensaje, solucion
        else:
            solucion = "{:.5f}".format(x)
            mensaje = "Fracaso en " + str(niter) + " iteraciones"
            return resultados, mensaje, None
    else:
        mensaje = "El intervalo es inadecuado"
        return None, mensaje, None


