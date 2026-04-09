#!/usr/bin/env python

from qr import qr
from gram_schmidt import matmul

def eigenvals(A: list[list[float]], n: int = 100) -> list[float]:
    """
    Realiza n iteraciones del algoritmo QR para calcular 
    los eigenvalores de A

    Devuelve la estimación de los eigenvalores
    """
    # Iniciamos con nuestra matriz A (es decir, A^(0) = A)
    A_k = A
    
    for _ in range(n):
        # 1. Factorizamos la matriz actual
        Q, R = qr(A_k)
        
        # 2. Multiplicamos al revés (R * Q) para la siguiente iteración
        A_k = matmul(R, Q)
        
    # Después de n iteraciones, A_k debería ser aproximadamente triangular superior.
    # Los valores propios se encuentran en la diagonal principal.
    eigenvalues = []
    for i in range(len(A_k)):
        eigenvalues.append(A_k[i][i])
        
    return eigenvalues