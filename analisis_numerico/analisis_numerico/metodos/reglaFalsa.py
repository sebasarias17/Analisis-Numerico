import math

def regla_falsa(f, x0, x1, tol, max_iter):

    iter = 0
    error = tol + 1

    output_file = 'regla_falsa_resultados.txt'

    with open(output_file, 'w') as file:
        header = 'Iteración\t x0\t\t x1\t\t x2\t\t f(x2)\t\t Error\n'
        print(header, end='')
        file.write(header)

        while error > tol and iter < max_iter:
            x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))  

            error = abs(x2 - x1)  

            line = f'{iter}\t\t {x0:.6f}\t {x1:.6f}\t {x2:.6f}\t {f(x2):.6f}\t {error:.6f}\n'
            print(line, end='')
            file.write(line)

            if f(x0) * f(x2) < 0:
                x1 = x2
            else:
                x0 = x2

            iter += 1 

    return x2, error

def funcion_ejemplo(x):
    return (math.exp(-2 * x + 8) - x) - ((-math.log(x)) - x + 8)

# Ejemplo de uso
x0 = 1.0
x1 = 2.0
tol = 1e-6
max_iter = 100

raiz, error = regla_falsa(funcion_ejemplo, x0, x1, tol, max_iter)
print(f'\nRaíz: {raiz}, Error: {error}')