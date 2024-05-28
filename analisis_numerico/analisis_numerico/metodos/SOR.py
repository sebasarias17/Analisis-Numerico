import numpy as np
import pandas as pd

def find_eig(A1):
    eigen = np.linalg.eigvals(A1)
    abs_eigen = np.abs(eigen)
    return round(np.max(abs_eigen), 3)

def str_to_matrix(matrix_str):
    rows = matrix_str.strip().split(';')
    matrix = np.array([[float(num) for num in row.split(',')] for row in rows])
    return matrix

def SOR(A_str, b_str, x0_str, tol, niter, w=1):
    A = str_to_matrix(A_str)
    b = str_to_matrix(b_str).flatten()
    x0 = str_to_matrix(x0_str).flatten()

    def find_parts(matrix):
        D = np.diag(np.diag(matrix))
        L = np.tril(matrix, k=-1) * -1  # Lower triangular matrix excluding the diagonal
        U = np.triu(matrix, k=1) * -1
        return D, L, U

    D, L, U = find_parts(A)
    
    try:
        DL = np.linalg.inv(D - w * L)
    except np.linalg.LinAlgError:
        print("No puede hacerse la matriz inversa")
        return None
    
    Tw = np.dot(DL, (1 - w) * D + w * U)
    Cw = np.dot(w * DL, b)
    i = 0

    EDD = find_eig(Tw)
    if EDD < 1:
        print("Vamos bien, cumple con el teorema de los eigenvalues")
    else:
        print("No cumple con el teorema de los eigenvalues")
        return None

    error = tol + 1
    results = []

    while error > tol and i < niter:
        i += 1
        x1 = np.dot(Tw, x0) + Cw
        error = abs(np.linalg.norm(x1 - x0, ord=np.inf))
        results.append([i, *x1, error])
        x0 = x1

    if i == niter:
        return None
    
    columns = ['Iteration'] + [f'x{j+1}' for j in range(len(x1))] + ['Error']
    df = pd.DataFrame(results, columns=columns)
    return df

