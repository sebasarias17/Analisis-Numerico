import numpy as np
import pandas as pd

def find_eig(A1):
    eigen = np.linalg.eigvals(A1)
    abs_eigen = np.abs(eigen)
    return round(np.max(abs_eigen), 3)

def str_to_matrix(matrix_str):
    rows = matrix_str.strip().split(';')
    try:
        matrix = np.array([[float(num) for num in row.split(',')] for row in rows])
    except ValueError as e:
        raise ValueError(f"Error converting string to matrix: {e}")
    return matrix

def jacobi_Seidel(A_str, b_str, x0_str, tol, niter, met):
    # Convert string inputs to matrices/vectors
    A = str_to_matrix(A_str)
    b = str_to_matrix(b_str).flatten()
    x0 = str_to_matrix(x0_str).flatten()

    def find_parts(matrix):
        D = np.diag(np.diag(matrix))
        L = np.tril(matrix, k=-1) * -1  # Lower triangular matrix excluding the diagonal
        U = np.triu(matrix, k=1) * -1
        return D, L, U
    
    D, L, U = find_parts(A)
    if met == 0:
        try:
            D_inv = np.linalg.inv(D)
        except np.linalg.LinAlgError:
            print("La matriz no tiene inversa")
            return None, None
        T = np.dot(D_inv, (L + U))
        C = np.dot(D_inv, b)
    else:
        try:
            DL_inv = np.linalg.inv(D - L)
        except np.linalg.LinAlgError:
            print("La matriz no tiene inversa")
            return None, None
        T = np.dot(DL_inv, U)
        C = np.dot(DL_inv, b)
    
    i = 0
    EDD = find_eig(T)
    if EDD < 1:
        print("Vamos bien")
    
    error = tol + 1
    iterations_data = []

    while error > tol and i < niter:
        i += 1
        x1 = np.dot(T, x0) + C
        error = abs(np.linalg.norm(x1 - x0, ord=np.inf))
        iterations_data.append([i] + list(x1) + [error])
        x0 = x1
    
    if i == niter:
        print("Reached maximum number of iterations without convergence.")
        return None, None
    
    columns = ['Iteration'] + [f'x{j+1}' for j in range(len(x0))] + ['Error']
    df_iterations = pd.DataFrame(iterations_data, columns=columns)
    return df_iterations, i

