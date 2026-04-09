#!/usr/bin/env python

"""
Realiza la factorización QR de una matriz
"""

# Corregimos los imports para usar las funciones que sí definimos en el entregable 1
from gram_schmidt import transpose, dot, proj, normalize

 def qr(M: list[list[float]]) -> tuple[list[list[float]], list[list[float]]]:
      """Realiza la factorización QR de una matriz M"""
    
    # Q como lista de columnas ortonormales
    Q_cols = gm(M)
    
    # Convertimos Q a formato fila (matriz estándar)
    Q = list(map(list, zip(*Q_cols)))
    
    # Transpuestas para trabajar por columnas
    Qt = transpose(Q)
    M_cols = transpose(M)
    
    # Construcción de R
    R = [[dot(qi, aj) for aj in M_cols] for qi in Qt]
    
    return Q, R
