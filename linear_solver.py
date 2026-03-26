#!/usr/bin/env python

from gram_schmidt import matvec
from qr import qr

def solve(A: list[list[float]], b:list[float]) -> list[float]:
    """Soluciona el sistema de ecuaciones lineales Ax = b"""
    x = ...
    Q, R = A 
    Qb = matvec(Q, b)
    ...
    return x
