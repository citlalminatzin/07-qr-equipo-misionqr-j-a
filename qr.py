#!/usr/bin/env python

"""
Realiza la factorización QR de una matriz
"""

# Corregimos los imports para usar las funciones que sí definimos en el entregable 1
from gram_schmidt import transpose, dot, proj, normalize

def qr(M: list[list[float]]) -> tuple[list[list[float]], list[list[float]]]:
    """Realiza la factorización QR de una matriz M"""
    
    # 1. Obtener las columnas de M
    # Es mucho más fácil trabajar si trasponemos M, ya que así iteramos directamente
    # sobre sus columnas (los vectores v_1, v_2, ..., v_n de tu teoría).
    V = transpose(M)
    Q_cols = []
    
    # 2. Proceso de Gram-Schmidt para construir las columnas de Q
    for v in V:
        u = list(v)  # Copiamos la columna actual para no modificar la original
        
        for e in Q_cols:
            # Restamos la proyección de 'v' sobre cada vector ortonormal 'e' previo.
            # Ojo: la función proj(u, v) proyecta el primer argumento sobre el segundo.
            p = proj(v, e)
            u = [ui - pi for ui, pi in zip(u, p)]
        
        # Normalizamos el vector u_k para obtener e_k y lo guardamos
        e_k = normalize(u)
        Q_cols.append(e_k)
        
    # Las columnas ortonormales forman Q, pero como en Python las matrices
    # son listas de filas, trasponemos de vuelta.
    Q = transpose(Q_cols)
    
    # 3. Construcción de la matriz triangular superior R
    # Sabemos que R_ij = <e_i, v_j> si i <= j, y 0 en caso contrario.
    R = []
    for i, e_i in enumerate(Q_cols):
        row_R = []
        for j, v_j in enumerate(V):
            if i <= j:
                # Producto punto entre la columna i de Q y la columna j de M
                row_R.append(dot(e_i, v_j))
            else:
                # Todo lo que está por debajo de la diagonal es cero
                row_R.append(0.0)
        R.append(row_R)
        
    return Q, R