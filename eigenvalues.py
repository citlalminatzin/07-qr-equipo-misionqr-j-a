#!/usr/bin/env python

from qr import qr
from gram_schmidt import matmul

def eigenvals(A: list[list[float]], n: int = 100) -> list[float]:
    """
    Realiza n iteraciones del algoritmo QR para calcular 
    los eigenvalores de A
    """
    
    Ak = A  # copia lógica (si quieres, puedes clonar profundo)
    
    for _ in range(n):
        Q, R = qr(Ak)
        Ak = matmul(R, Q)
    
    # Eigenvalores ≈ diagonal de Ak
    return [Ak[i][i] for i in range(len(Ak))]
