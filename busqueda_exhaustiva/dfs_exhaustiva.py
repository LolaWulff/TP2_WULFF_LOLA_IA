#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DFS (búsqueda exhaustiva en profundidad) sobre el eje H.
Imprime orden de expansión y camino solución.
"""

# Parámetros ajustables
A = -7            # meta (a la izquierda de B en este ejemplo)
B = 0             # inicio teórico
DELTA = 1         # paso ΔH
BOUNDS = (-12, 12)  # límites físicos
LEFT_FIRST = True   # prioridad de sucesores: izquierda luego derecha

def neighbors(x: int):
    first  = x - DELTA if LEFT_FIRST else x + DELTA
    second = x + DELTA if LEFT_FIRST else x - DELTA
    for nx in (first, second):
        if BOUNDS[0] <= nx <= BOUNDS[1]:
            yield nx

def dfs(start: int, goal: int):
    stack = [start]          # pila LIFO
    visited = set()
    parent = {start: None}   # para reconstruir camino
    expanded = []            # orden de expansión

    while stack:
        x = stack.pop()
        if x in visited:
            continue
        visited.add(x)
        expanded.append(x)
        if x == goal:
            break
        succs = list(neighbors(x))
        # apilar en orden inverso para que el primero generado salga antes
        for nx in reversed(succs):
            if nx not in parent:
                parent[nx] = x
            stack.append(nx)

    # reconstrucción de camino start→goal
    path = []
    if goal in parent or goal == start:
        n = goal
        while n is not None:
            path.append(n)
            n = parent.get(n)
        path.reverse()
    return expanded, path

if __name__ == "__main__":
    expanded, path = dfs(B, A)
    print("=== DFS (exhaustiva: primero en profundidad) ===")
    print("Orden de expansión:", expanded)
    print("Camino solución:   ", path, f"(longitud = {len(path)})")
