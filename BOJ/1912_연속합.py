# https://www.acmicpc.net/problem/1912

import sys

input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))

for i in range(1, n):
    m[i] = max(m[i], m[i - 1] + m[i])

print(max(m))
