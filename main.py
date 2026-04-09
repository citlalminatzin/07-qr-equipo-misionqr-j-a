#!/usr/bin/env python

import collections
import numbers

# Añadimos 'sin' a la importación estándar
from math import pi, sin

from linear_solver import solve

# linspace obtenido de (https://code.activestate.com/recipes/579000/)
class linspace(collections.abc.Sequence):
    """linspace(start, stop, num) -> linspace object
    
    Return a virtual sequence of num numbers from start to stop (inclusive).
    
    If you need a half-open range, use linspace(start, stop, num+1)[:-1].
    """
    
    def __init__(self, start, stop, num):
        if not isinstance(num, numbers.Integral) or num <= 1:
            raise ValueError('num must be an integer > 1')
        self.start, self.stop, self.num = start, stop, num
        self.step = (stop-start)/(num-1)
    def __len__(self):
        return self.num
    def __getitem__(self, i):
        if isinstance(i, slice):
            return [self[x] for x in range(*i.indices(len(self)))]
        if i < 0:
            i = self.num + i
        if i >= self.num:
            raise IndexError('linspace object index out of range')
        if i == self.num-1:
            return self.stop
        return self.start + i*self.step
    def __repr__(self):
        return '{}({}, {}, {})'.format(type(self).__name__,
                                       self.start, self.stop, self.num)
    def __eq__(self, other):
        if not isinstance(other, linspace):
            return False
        return ((self.start, self.stop, self.num) ==
                (other.start, other.stop, other.num))
    def __ne__(self, other):
        return not self==other
    def __hash__(self):
        return hash((type(self), self.start, self.stop, self.num))  

def vandermonde_matrix(x: list[float]) -> list[list[float]]:
    """Genera una matriz de Vandermonde"""
    n = len(x)
    # Por cada punto xi en la lista x, generamos una fila.
    # La fila contiene xi elevado a la potencia j, desde j=0 hasta j=n-1
    return [[xi**j for j in range(n)] for xi in x]

def interpolate(points: list[float], values: list[float]) -> list[float]:
    """
    Interpola un polinomio a los puntos

    Devuelve los coeficientes del polinomio
    """
    M = vandermonde_matrix(points)
    return solve(M, values)


def interpolate_sine(n: int) -> list[float]:
    """Recibe la cantidad de puntos a interpolar la función seno"""
    lim_inf: float = 0
    lim_sup: float = 2 * pi
    
    # linspace se comporta como una secuencia, podemos convertirla a lista
    points = list(linspace(lim_inf, lim_sup, n))
    
    # Evaluamos la función seno en cada punto generado
    values = [sin(p) for p in points]
    
    # Llamamos a la función que arma el sistema y lo resuelve
    return interpolate(points, values)


def main():
    """Función principal para probar la interpolación"""
    n_puntos = 5
    print(f"Calculando los coeficientes del polinomio que interpola sin(x) con {n_puntos} puntos...\n")
    
    coeficientes = interpolate_sine(n_puntos)
    
    print("El polinomio aproximado es:")
    terminos = []
    for i, c in enumerate(coeficientes):
        if i == 0:
            terminos.append(f"{c:.4f}")
        elif i == 1:
            terminos.append(f"{c:.4f}x")
        else:
            terminos.append(f"{c:.4f}x^{i}")
            
    print(" + ".join(terminos))

if __name__ == "__main__":
    main()
