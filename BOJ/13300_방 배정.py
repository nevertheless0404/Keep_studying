# https://www.acmicpc.net/problem/13300

import sys, math

input = sys.stdin.readline

n, k = map(int, input().split())
info = [[0] * 7 for _ in range(3)]

for _ in range(n):
    s, y = map(int, input().split())
    info[s][y] += 1

room = 0


for i in info:
    for j in i:
        room += math.ceil(j / k)

print(room)
