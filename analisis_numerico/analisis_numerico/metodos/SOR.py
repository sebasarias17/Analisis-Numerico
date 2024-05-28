import numpy as np
def find_eig(A1):
    eigen=np.linalg.eigvals(A1)
    abs=np.abs(eigen)
    return round(np.max(abs),3)
  def SOR(A, b, x0,tol=1e-10, niter=100, w=1 ):
   def find_parts(matrix):
      D = np.diag(np.diag(matrix))
      L = np.tril(matrix, k=-1)*-1  # Lower triangular matrix excluding the diagonal
      U = np.triu(matrix, k=1)*-1
      return D,L,U
   D,L,U=find_parts(A)
   try:
      DL=np.linalg.inv(D-w*L)
   except:
      print("No puede hacerse la matriz inversa")
      return None, None
   Tw=np.dot(DL, (1-w)*D + w*U)
   Cw=np.dot(w*DL, b)
   i=0
   EDD=find_eig(Tw)
   if EDD<1:
      print("Vamos bien, cumple con el teorema de los eigenvalues")
   error=tol+1
   while error>tol and i<niter:
      i+=1
      x1=np.dot(Tw,x0)+Cw
      error=abs(np.linalg.norm(x1-x0, ord=np.inf))
      x0=x1
   if i==niter:
      return None, None
   return x1, i
   
