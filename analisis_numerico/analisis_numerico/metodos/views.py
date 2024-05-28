# views.py
import numpy as np
import matplotlib.pyplot as plt
from django.shortcuts import render
from analisis_numerico.metodos.puntoFijo import pf
from analisis_numerico.metodos.biseccion import biseccion
from analisis_numerico.metodos.simpson38 import (
    simpson_38,
    funcion_ejemplo,
    graficar_funcion as graficar_funcion_simpson38,
)
from analisis_numerico.metodos.simpson13 import (
    simpson13,
    funcion_a_integrar,
    plot_function_and_points as graficar_funcion_simpson13,
)
from analisis_numerico.metodos.trapeciomastabla import (
    trapecio,
    funcion_ejemplo as funcion_trapecio,
)
from analisis_numerico.metodos.biseccion import biseccion
from analisis_numerico.metodos.reglaFalsa import regla_falsa
from analisis_numerico.metodos.secante import secante
from analisis_numerico.metodos.inputFixed import CorregirFuncion
from analisis_numerico.metodos.SOR import SOR
from analisis_numerico.metodos.JacobiSeidel import jacobi_Seidel
import csv


def home(request):
    return render(request, "home.html")


def cap1(request):
    A = b = X0 = tol = itera = result = error = form_type  =None
    if request.method == "POST":
        form_type = request.POST.get("form_type")
        if form_type == "Bisección":
            function = request.POST.get("Funcion")
            xi = float(request.POST.get("Xi"))
            xs = float(request.POST.get("Xs"))
            tol = float(request.POST.get("tol"))
            iteraciones = int(request.POST.get("n"))
            function = CorregirFuncion(function)
            result = biseccion(function, xi, xs, tol, iteraciones)
            try:
               result = result.to_html(classes='table table-bordered', index=False)
               print(result)
            except:
                pass
        if form_type == "Reglafalsa":
            function = request.POST.get("Funcion")
            x0 = float(request.POST.get("X0"))
            x1 = float(request.POST.get("X1"))
            tol = float(request.POST.get("tol"))
            iteraciones = int(request.POST.get("n"))
            result = regla_falsa(function, x0, x1, tol, iteraciones)
            try:
               result = result[0].to_html(classes='table table-bordered', index=False)
            except:
                pass
        if form_type == "Puntofijo":
            functionf = request.POST.get("Funcionf")
            iteraciones = int(request.POST.get("niter"))
            x0 = float(request.POST.get("X0"))
            functiong = request.POST.get("Funciong")
            tol = float(request.POST.get("tolerancia"))
            result = pf(x0, tol,iteraciones,functionf,functiong)
            try:
                result = result.to_html(classes ='table table-bordered', index = False)
            except:
                pass
        if form_type == "Newton":
            print("Newton")
        if form_type == "Secante":
            function = request.POST.get("Funcion")
            x0 = float(request.POST.get("X0"))
            x1 = float(request.POST.get("X1"))
            tol = float(request.POST.get("tol"))
            function = CorregirFuncion(function)
            result =secante(function, x0, x1, tol)
            try:
               result = result.to_html(classes='table table-bordered', index=False)
            except:
                pass
        if form_type == "Newton2":
            print("Newton2")
    return render(request, "cap1.html",
        {
            "result": result,
            "selected_method": form_type,
        })


def cap4(request):
    result = None
    error = None
    selected_method = None
    a = b = n = ""
    img_data = None
    table_html = None

    if request.method == "POST":
        selected_method = request.POST.get("method")
        try:
            a = float(request.POST.get("a"))
            b = float(request.POST.get("b"))
            n = int(request.POST.get("n"))

            if selected_method == "simpson38":
                result = simpson_38(funcion_ejemplo, a, b, n)
                img_data = graficar_funcion_simpson38(funcion_ejemplo, a, b, n, result)
            elif selected_method == "simpson13":
                result = simpson13(a, b, n, funcion_ejemplo)
                x_vals = np.linspace(a, b, n + 1)
                fx_vals = [funcion_ejemplo(x) for x in x_vals]
                img_data = graficar_funcion_simpson13(
                    a, b, funcion_ejemplo, x_vals, fx_vals
                )
            elif selected_method == "trapecio":
                func_input = "1.5 * x**2 + 4 * x + 3500"
                result, table_html, img_data = trapecio(
                    a, b, n, funcion_trapecio, func_input
                )
            else:
                error = "Método no válido seleccionado."
        except ValueError as e:
            error = str(e)
        except Exception as e:
            error = "Error en el cálculo. Verifique los datos ingresados."

    return render(
        request,
        "cap4.html",
        {
            "result": result,
            "error": error,
            "selected_method": selected_method,
            "a": a,
            "b": b,
            "n": n,
            "img_data": img_data,
            "table_html": table_html,
        },
    )


def cap2(request):
    A = b = X0 = tol = itera = result = error = None
    selected_method = None
    if request.method == "POST":
        selected_method = request.POST.get("method")
        if selected_method == "SOR":
            A = request.POST.get("a")
            b = request.POST.get("b")
            X0 = request.POST.get("X0")
            tol = float(request.POST.get("tol"))
            itera = int(request.POST.get("n"))
            result = SOR(A, b, X0, tol, itera)
            try:
               result = result.to_html(classes='table table-bordered', index=False)
            except:
                pass
        if selected_method == "JacobiSeidel":
            A = request.POST.get("a")
            b = request.POST.get("b")
            X0 = request.POST.get("X0")
            tol = float(request.POST.get("tol"))
            itera = int(request.POST.get("n"))
            metodo = int(request.POST.get("metodo"))
            result = jacobi_Seidel(A, b, X0, tol, itera, metodo)
            try:
               result = result[0].to_html(classes='table table-bordered', index=False)
            except:
                pass  
    return render(
        request,
        "cap2.html",
        {
            "result": result,
            "Matriz A": A,
            "error": tol,
            "selected_method": selected_method,
            "X0": X0,
            "b": b,
            "n": itera,
        },
    )


def cap3(request):
    return render(request, "cap3.html")
