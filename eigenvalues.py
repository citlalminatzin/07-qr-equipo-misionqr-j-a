#!/usr/bin/env python

from qr import qr
from gram_schmidt import matmul

def eigenvals(A:list[list[float]], n:int = 100)->list[float]:
    """
    Realiza n iteraciones del algoritmo QR para calcular 
    los eigenvalores de A

    Devuelve la estimación de los eigenvalores
    """
    Q,R = qr(A)
    for _ in range(n):
        ...
    return ...
