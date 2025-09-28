#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Greedy Best-First Search (Primero el mejor) sobre el eje H.
Imprime orden de expansión y camino solución.
"""

import heapq

# ===== Parámetros del problema (ajustables) =====
A = 7           # Meta (a la derecha en este ejemplo)
B = 0           # Inicio teórico
DELTA = 1       # paso ΔH
BOUNDS = (-12, 12)

def h(x: int) -> int:
    """Heurística: distancia estimada a la meta."""
    return abs(A - x)

def neighbors(x: int):
    for nx in (x - DELTA, x + DELTA):
        if BOUNDS[0] <= nx <= BOUNDS[1]:
            yield nx

def greedy(start: int, goal: int):
    parent = {start: None}
    visited = set()
    expansion_order = []
    frontier = [(h(start), start)]
    in_frontier = {start}

    while frontier:
        _, x = heapq.heappop(frontier)
        in_frontier.discard(x)
        if x in visited:
            continue
        visited.add(x)
        expansion_order.append(x)

        if x == goal:
            break

        for nx in neighbors(x):
            if nx not in visited and nx not in in_frontier:
                parent[nx] = x
                heapq.heappush(frontier, (h(nx), nx))
                in_frontier.add(nx)

    # reconstrucción de camino
    path = []
    if goal in parent or goal == start:
        n = goal
        while n is not None:
            path.append(n)
            n = parent.get(n)
        path.reverse()
    return expansion_order, path

if __name__ == "__main__":
    expanded, path = greedy(B, A)
    print("=== Greedy Best-First (Primero el mejor) ===")
    print("Orden de expansión:", expanded)
    print("Camino solución:   ", path, f"(longitud = {len(path)})")
