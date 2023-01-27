# https://www.acmicpc.net/problem/15686

from itertools import combinations
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            house.append((i, j))
        elif board[i][j] == 2:
            chicken.append((i, j))

minv = float("inf")
for ch in combinations(chicken, m):
    sumv = 0
    for home in house:
        sumv += min([abs(home[0] - i[0]) + abs(home[1] - i[1]) for i in ch])
        if minv <= sumv:
            break
    if sumv < minv:
        minv = sumv

print(minv)
