# views.py
import numpy as np
import matplotlib.pyplot as plt
from django.shortcuts import render
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
from analisis_numerico.metodos.vandermon import interpolate_vandermonde as vandermonde_logic
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponse
from .forms import VandermondeForm
from .forms import NewtonForm
import io
import base64
from analisis_numerico.metodos.newton_interpolante import newton_interpolating_polynomial, polynomial_expression
from django.http import FileResponse, Http404
import uuid
from .forms import NewtonRaphsonForm
from .newton_raphson import newton_raphson
from .inputFixed import CorregirFuncion


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
            print("pf")
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

def interpolate_vandermonde(request):
    if request.method == 'POST':
        form = VandermondeForm(request.POST)
        if form.is_valid():
            x_values = list(map(float, form.cleaned_data['x_values'].split(',')))
            y_values = list(map(float, form.cleaned_data['y_values'].split(',')))

            poly = vandermonde_logic(x_values, y_values)

            poly_text = str(poly)
            txt_filename = f'polynomial_{uuid.uuid4().hex}.txt'
            txt_path = default_storage.save(txt_filename, ContentFile(poly_text.encode('utf-8')))

            plt.figure()
            xp = np.linspace(min(x_values) - 10, max(x_values) + 10, 1000)
            plt.plot(x_values, y_values, 'o', label='Puntos de datos')
            plt.plot(xp, [poly(xi) for xi in xp], '-', label='Polinomio de Vandermonde')
            plt.axhline(0, color='black', linewidth=0.5)
            plt.axvline(0, color='black', linewidth=0.5)
            plt.legend()
            
            x_margin = (max(x_values) - min(x_values)) * 1.5
            y_margin = (max(y_values) - min(y_values)) * 1.5
            plt.xlim([min(x_values) - x_margin, max(x_values) + x_margin])
            plt.ylim([min(y_values) - y_margin, max(y_values) + y_margin])

            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            image_filename = f'plot_{uuid.uuid4().hex}.png'
            image_path = default_storage.save(image_filename, ContentFile(buf.getvalue()))

            image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            buf.close()

            return render(request, 'results.html', {
                'method_name': 'Vandermonde',
                'poly': poly_text,
                'image_url': image_path,
                'txt_url': txt_path,
                'image_base64': image_base64
            })
    else:
        form = VandermondeForm()
    return render(request, 'interpolate.html', {'form': form})

def interpolate_newton(request):
    if request.method == 'POST':
        form = NewtonForm(request.POST)
        if form.is_valid():
            x_values = list(map(float, form.cleaned_data['x_values'].split(',')))
            y_values = list(map(float, form.cleaned_data['y_values'].split(',')))

            poly, coef = newton_interpolating_polynomial(x_values, y_values)
            poly_expr = polynomial_expression(coef, x_values)

            poly_text = f'Coeficientes: {coef}\nPolinomio: {poly_expr}'
            txt_filename = f'newton_polynomial_{uuid.uuid4().hex}.txt'
            txt_path = default_storage.save(txt_filename, ContentFile(poly_text.encode('utf-8')))

            plt.figure()
            xp = np.linspace(min(x_values) - 10, max(x_values) + 10, 1000)
            plt.plot(x_values, y_values, 'o', label='Puntos de datos')
            plt.plot(xp, [poly(xi) for xi in xp], '-', label='Polinomio de Newton')
            plt.axhline(0, color='black', linewidth=0.5)
            plt.axvline(0, color='black', linewidth=0.5)
            plt.legend()

            x_margin = (max(x_values) - min(x_values)) * 1.5
            y_margin = (max(y_values) - min(y_values)) * 1.5
            plt.xlim([min(x_values) - x_margin, max(x_values) + x_margin])
            plt.ylim([min(y_values) - y_margin, max(y_values) + y_margin])

            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            image_filename = f'newton_plot_{uuid.uuid4().hex}.png'
            image_path = default_storage.save(image_filename, ContentFile(buf.getvalue()))

            image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            buf.close()

            return render(request, 'results.html', {
                'method_name': 'Newton',
                'poly': poly_expr,
                'image_url': image_path,
                'txt_url': txt_path,
                'image_base64': image_base64
            })
    else:
        form = NewtonForm()
    return render(request, 'interpolate.html', {'form': form})



def newton_raphson(f, df, x0, tol, max_iter):
    x = x0
    table = []
    decimal_places = abs(int(np.log10(tol)))
    
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            break
        x_new = x - fx / dfx
        error = abs(x_new - x)
        if i == 0:
            table.append((i, f"{x:.{decimal_places}f}", f"{fx:.{decimal_places}e}", ''))
        else:
            table.append((i, f"{x:.{decimal_places}f}", f"{fx:.{decimal_places}e}", f"{error:.{decimal_places}e}"))
        if error < tol:
            table.append((i + 1, f"{x_new:.{decimal_places}f}", f"{f(x_new):.{decimal_places}e}", f"{error:.{decimal_places}e}"))
            break
        x = x_new
    return x, table

def newton_raphson_view(request):
    if request.method == 'POST':
        form = NewtonRaphsonForm(request.POST)
        if form.is_valid():
            function = form.cleaned_data['function']
            derivative = form.cleaned_data['derivative']
            x0 = form.cleaned_data['x0']
            tol = form.cleaned_data['tolerance']
            max_iter = form.cleaned_data['max_iterations']

            function = CorregirFuncion(function)
            derivative = CorregirFuncion(derivative)

            try:
                f = eval(f"lambda x: {function}", {"np": np})
                df = eval(f"lambda x: {derivative}", {"np": np})

                root, table = newton_raphson(f, df, x0, tol, max_iter)

                txt_content = "Iter\t x\t f(x)\t Error\n" + "\n".join(
                    f"{i}\t{xi}\t{fxi}\t{error}" for i, xi, fxi, error in table
                )

                txt_filename = f"newton_raphson_{uuid.uuid4().hex}.txt"
                txt_path = default_storage.save(txt_filename, ContentFile(txt_content.encode('utf-8')))

                xp = np.linspace(x0 - 10, x0 + 10, 400)
                yp = [f(xi) for xi in xp]
                dyp = [df(xi) for xi in xp]

                plt.figure()
                plt.plot(xp, yp, label="f(x)")
                plt.plot(xp, dyp, label="f'(x)", linestyle='--')
                plt.axhline(0, color='black', linewidth=0.5)
                plt.axvline(0, color='black', linewidth=0.5)
                plt.scatter([float(xi) for _, xi, _, _ in table if xi != ''], [f(float(xi)) for _, xi, _, _ in table if xi != ''], color='red', zorder=5)
                plt.legend()

                buf = io.BytesIO()
                plt.savefig(buf, format='png')
                buf.seek(0)
                image_filename = f"newton_raphson_{uuid.uuid4().hex}.png"
                image_path = default_storage.save(image_filename, ContentFile(buf.getvalue()))

                image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
                buf.close()

                return render(request, 'newton_raphson_results.html', {
                    'form': form,
                    'root': root,
                    'table': table,
                    'txt_url': txt_path,
                    'image_base64': image_base64,
                    'image_url': image_path
                })
            except Exception as e:
                return render(request, 'newton_raphson.html', {'form': form, 'error': str(e)})
    else:
        form = NewtonRaphsonForm()
    return render(request, 'newton_raphson.html', {'form': form})


def download_file(request, filename):
    file_path = default_storage.path(filename)
    try:
        return FileResponse(open(file_path, 'rb'), as_attachment=True)
    except FileNotFoundError:
        raise Http404("File not found")
