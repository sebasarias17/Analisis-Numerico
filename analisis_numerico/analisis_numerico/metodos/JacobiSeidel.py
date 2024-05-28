import numpy as np
def find_eig(A1):
    eigen=np.linalg.eigvals(A1)
    abs=np.abs(eigen)
    return round(np.max(abs),3)
  #Gauss Seidel será 1 y Jacobi será 0
def jacobi_Seidel(A, b,x0,  tol=1e-10, niter=100, met=0):
    def find_parts(matrix):
        D = np.diag(np.diag(matrix))
        L = np.tril(matrix, k=-1)*-1  # Lower triangular matrix excluding the diagonal
        U = np.triu(matrix, k=1)*-1
        return D,L,U
    
    D,L,U=find_parts(A)
    if met==0:
        try:
            D_1=np.linalg.inv(D)
        except:
            print("La matriz no tiene inversa")
        T=np.dot(D_1,(L+U))
        C=np.dot(D_1,b)
    else:
        try:
            DL=np.linalg.inv(D-L)
        except:
            print("La matriz no tiene inversa")
            return None, None
        T=np.dot(DL,U)
        C=np.dot(DL, b)
    i=0
    EDD=find_eig(T)
    if EDD<1:
        print("Vamos bien")
    error=tol+1
    while error>tol and i<niter:
        i+=1
        x1=np.dot(T,x0)+C
        error=abs(np.linalg.norm(x1-x0, ord=np.inf))
        x0=x1
    if i==niter:
        return None, None
    return x1,i
