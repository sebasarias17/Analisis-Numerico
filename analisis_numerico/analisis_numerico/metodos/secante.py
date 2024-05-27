def secante(f, X0, X1, tolerancia):
 
  n = 0
  error = 1

  documento = 'secante.txt'
  with open(documento, 'w') as file:
    header = 'Iteración\tXn\t\tf(Xn)\t\tError'
    file.write(header)
    
    while error > tolerancia:
      n += 1
      Xn1 = X1 - ((f(X1) * (X1 - X0)) / (f(X1) - f(X0)))
      error = abs(Xn1 - X1)
      line = f'{n}\t\t{Xn1:.8f}\t{f(Xn1):.8f}\t{error:.8f}'
      file.write(line)
      X0 = X1
      X1 = Xn1
    

def f(x):
  return (2**(-x)) * (-1 + x) + x**(2/3) - 76

X0 = 0.5 
X1 = 1.0  
tolerancia = 1e-6  

secante(f, X0, X1, tolerancia)