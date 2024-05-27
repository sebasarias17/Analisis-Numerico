import numpy as np
import sympy as sp

def RuKu4(a, b, N, y0):
    # Definir variables simbólicas
    t = sp.Symbol('t')
    y = sp.Symbol('y')
    var = [t, y]
    
    # Definir la función f
    f = 8 * sp.cos(t * y) + t
    
    h = (b - a) / N
    time = a
    yout = y0
    
    # Evaluar f en el tiempo final
    for k in range(N):
        K = np.zeros(4)
        K[0] = f.subs([(var[0], time), (var[1], yout)]).evalf()
        K[1] = f.subs([(var[0], time + 0.5 * h), (var[1], yout + 0.5 * h * K[0])]).evalf()
        K[2] = f.subs([(var[0], time + 0.5 * h), (var[1], yout + 0.5 * h * K[1])]).evalf()
        K[3] = f.subs([(var[0], time + h), (var[1], yout + h * K[2])]).evalf()
        
        yout = yout + (1/6) * (K[0] + 2 * K[1] + 2 * K[2] + K[3]) * h
        time = time + h
    
    # Redondear los resultados
    yout = round(yout, 3)
    time = round(time, 2)
    
    return yout, time

def main():
    # Solicitar datos al usuario
    a = float(input("Ingrese el valor de a (inicio del intervalo): "))
    b = float(input("Ingrese el valor de b (fin del intervalo): "))
    N = int(input("Ingrese el número de divisiones N: "))
    y0 = float(input("Ingrese la condición inicial para y0: "))

    yout, final_time = RuKu4(a, b, N, y0)
    
    print(f"Resultado final de yout: {yout:.3f}")
    print(f"Tiempo final: {final_time:.2f} segundos")

if __name__ == "__main__":
    main()
