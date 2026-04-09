#!/usr/bin/env python

from gram_schmidt import matvec, transpose
from qr import qr

def solve(A: list[list[float]], b: list[float]) -> list[float]:
    """Soluciona el sistema de ecuaciones lineales Ax = b"""
    
    Q, R = qr(A)
    
    # y = Q^T b
    Qt = transpose(Q)
    y = matvec(Qt, b)
    
    # Sustitución hacia atrás (R es triangular superior)
    n = len(R)
    x = [0.0] * n
    
    for i in range(n - 1, -1, -1):
        suma = sum(R[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (y[i] - suma) / R[i][i]
    
    return x
