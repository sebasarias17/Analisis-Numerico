from django.shortcuts import render
from analisis_numerico.metodos.trapecio import trapecio
from analisis_numerico.metodos.biseccion import biseccion


def home(request):
    return render(request, 'home.html')


def cap1(request):
    if request.method == 'POST':
        request.POST.get()
    return render(request, 'cap1.html')




































def cap2(request):
    return render(request, 'cap2.html')

def cap3(request):
    if request.method == 'POST':
        pass
    return render(request, 'cap3.html')

def cap4(request):
    context = {}
    if request.method == 'POST':
        funcion = request.POST.get('Funcion')
        a = request.POST.get('Cota superior')
        b = request.POST.get('Cota inferior')
        niter = request.POST.get('n')

        errors = []
        if not funcion:
            errors.append("La función es requerida.")
        if not a:
            errors.append("La cota superior es requerida.")
        if not b:
            errors.append("La cota inferior es requerida.")
        if not niter:
            errors.append("El número de iteraciones es requerido.")
        else:
            try:
                niter = int(niter)
            except ValueError:
                errors.append("El número de iteraciones debe ser un número entero.")

        if not errors:
           
            print(funcion)
            print(a)
            print(b)
            print(niter)
            funcion = str(funcion) 
            a = float(a)
            b = float(b)
            niter = int(niter)
            context['funcion'] = funcion
            context['a'] = a
            context['b'] = b
            context['niter'] = niter
            trapecio(a,b,niter,funcion)
        else:
            context['errors'] = errors

    return render(request, 'cap4.html', context)

