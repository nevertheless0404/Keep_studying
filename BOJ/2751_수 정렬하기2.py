# https://www.acmicpc.net/problem/2751

import sys
input = sys.stdin.readline

n = int(input())
l = []

for i in range(n):
    l.append(int(input()))

l.sort()

for j in l:
    print(j)