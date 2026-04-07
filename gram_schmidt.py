#!/usr/bin/env python
import math


"""
Calcula la factorización de gram-schmidt
para una matriz de tamaño n
"""

def dot(x: list[float], y: list[float]) -> float:
    """Producto punto entre dos vectores"""
    if len(x) != len(y):
        raise ValueError("Los vectores deben tener la misma longitud")

    return sum(a * b for a, b in zip(x, y))



def transpose(M: list[list[float]]) -> list[tuple[float]]:
    """Devuelve traspuesta de una matriz"""
    return list(zip(*M))



def matmul(A:list[list[float]], B:list[list[float]])->list[list[float]]:
    """Multiplicación de dos matrices"""

    Bt = transpose(B)  # columnas de B como filas

    return [
        [dot(fila_A, col_B) for col_B in Bt]
        for fila_A in A
           ]


def matvec(A: list[list[float]], v: list[float]) -> list[float]:
    """Multiplicación de matriz por un vector"""

    if not A:
        return []

    n = len(A[0])

    if len(v) != n:
        raise ValueError("Dimensiones incompatibles")

    return [dot(row, v) for row in A]


def norm(x:list[float])->float:
    """Obtiene la norma 2 de un vector"""
    return math.sqrt(sum(xi * xi for xi in x))


def proj(u:list[float], v:list[float])->list[float]:
    factor = dot(u, v) / dot(v, v)
    return [factor * vi for vi in v]


def normalize(u: list[float]) -> list[float]:
    """Normaliza un vector"""

    n = norm(u)

    if n == 0:
        raise ValueError("No se puede normalizar el vector cero")

    return [ui / n for ui in u]


def matrix_to_str(matrix: list[list[float]])->str:
    """Convierte una matriz a texto"""
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    # return '\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix])
    return '\n'.join(table)
