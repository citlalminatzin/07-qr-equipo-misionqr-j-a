#!/usr/bin/env python

"""
Calcula la factorización de gram-schmidt
para una matriz de tamaño n
"""

def dot(x:list[float], y:list[float])->float:
    """Producto punto entre dos vectores"""
    return sum(xi * yi for xi, yi in zip(x, y))

def transpose(M:list[list[float]])->list[tuple[float]]:
    """Devuelve traspuesta de una matriz"""
    return list(zip(*M))

def matmul(A:list[list[float]], B:list[list[float]])->list[list[float]]:
    """Multiplicación de dos matrices"""
    B_T = transpose(B)
    return [[dot(row_A, col_B) for col_B in B_T] for row_A in A]

def matvec(A:list[list[float]], v:list[float]) -> list[float]:
    """Multiplicación de matriz por un vector"""
    return [dot(row, v) for row in A]

def norm(x:list[float])->float:
    """Obtiene la norma 2 de un vector"""
    return dot(x, x) ** 0.5

def proj(u:list[float], v:list[float])->list[float]:
    """Calcula la proyección de u en v"""
    scalar = dot(u, v) / dot(v, v)
    return [scalar * vi for vi in v]

def normalize(u:list[float])->list[float]:
    """Normaliza un vector"""
    n = norm(u)
    return [ui / n for ui in u]

def matrix_to_str(matrix: list[list[float]])->str:
    """Convierte una matriz a texto"""
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    return '\n'.join(table)
