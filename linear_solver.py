#!/usr/bin/env python

from gram_schmidt import matvec, transpose
from qr import qr

def solve(A: list[list[float]], b: list[float]) -> list[float]:
    """Soluciona el sistema de ecuaciones lineales Ax = b"""
    
    # 1. Factorizamos la matriz A
    Q, R = qr(A) 
    
    # 2. Multiplicamos la traspuesta de Q por b
    # Matemáticamente es Q^T * b (aunque el README lo llame Qb)
    Q_T = transpose(Q)
    y = matvec(Q_T, b) 
    
    # 3. Solucionamos el sistema triangular superior Rx = y
    # Empezamos desde la última fila hacia arriba (sustitución hacia atrás)
    n = len(R)
    x = [0.0] * n  # Preparamos nuestra lista de soluciones con ceros
    
    # Recorremos desde n-1 hasta 0 (de reversa)
    for i in range(n - 1, -1, -1):
        # Sumamos los coeficientes de las variables que ya calculamos
        suma = sum(R[i][j] * x[j] for j in range(i + 1, n))
        
        # Despejamos la incógnita actual (x_i)
        x[i] = (y[i] - suma) / R[i][i]
        
    return x