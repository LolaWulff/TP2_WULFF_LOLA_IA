#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BFS (búsqueda exhaustiva en anchura) sobre el eje H.
Imprime orden de expansión y camino solución.
"""

from collections import deque

# Parámetros ajustables
A = -7
B = 0
DELTA = 1
BOUNDS = (-12, 12)
LEFT_FIRST = True  # solo afecta el orden de generación dentro del mismo nivel

def neighbors(x: int):
    first  = x - DELTA if LEFT_FIRST else x + DELTA
    second = x + DELTA if LEFT_FIRST else x - DELTA
    for nx in (first, second):
        if BOUNDS[0] <= nx <= BOUNDS[1]:
            yield nx

def bfs(start: int, goal: int):
    q = deque([start])               # cola FIFO
    visited = set([start])
    parent = {start: None}
    expanded = []

    while q:
        x = q.popleft()
        expanded.append(x)
        if x == goal:
            break
        for nx in neighbors(x):
            if nx not in visited:
                visited.add(nx)
                parent[nx] = x
                q.append(nx)

    path = []
    if goal in parent or goal == start:
        n = goal
        while n is not None:
            path.append(n)
            n = parent.get(n)
        path.reverse()
    return expanded, path

if __name__ == "__main__":
    expanded, path = bfs(B, A)
    print("=== BFS (exhaustiva: primero en anchura) ===")
    print("Orden de expansión:", expanded)
    print("Camino solución:   ", path, f"(longitud = {len(path)})")
