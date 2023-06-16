#!/usr/bin/env python3

import sys

from common import print_tour, read_input
from solver_greedy import distance, solve

def set_dist(cities):
    N = len(cities)
    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
            return dist

def calculate_2opt_cost(tour, i, j, dist):
    N = len(tour)
    a, b = tour[i], tour[(i + 1) % N]
    c, d = tour[j], tour[(j + 1) % N]

    cost_before = dist[a][b] + dist[c][d]
    cost_after = dist[a][c] + dist[b][d]
    return cost_after - cost_before

def apply_2opt_exchange(tour, i, j):
    tmp = tour[i + 1: j + 1]
    tmp.reverse()
    tour[i + 1: j + 1] = tmp
    return tour

def solve_with_2opt(tour, dist):
    N = len(tour)
    cost_best = 0
    i_best, j_best = None, None
    
    for i in range(0, N-2):
        for j in range(i+2, N):
            if i == 0 and j ==N-1:
                continue
            
            cost = calculate_2opt_cost(tour, i, j, dist)
            if cost < cost_best:
                cost_best = cost
                i_best, j_best = i, j
                
    if cost_best < 0:
        tour_new = apply_2opt_exchange(tour, i_best, j_best)
        return tour_new
    else:
        return None

if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    dist = set_dist(read_input(sys.argv[1]))
    solve_with_2opt(tour, dist)
    print_tour(tour)