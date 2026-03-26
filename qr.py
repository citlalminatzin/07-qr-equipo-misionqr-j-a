#!/usr/bin/env python

"""
Realiza la factorización QR de una matriz
"""

from gram_schmidt import gm, transpose, dot

def qr(M:list[list[float]])->tuple[list[list[float]], list[list[float]]]:
    """Realiza la factorización QR de una matriz M"""
    Q = ...
    R = ...
    return Q,R
