# https://www.acmicpc.net/problem/15486

import sys

input = sys.stdin.readline

n = int(input())

t = []
p = []
dp = [0] * (n + 1)

for _ in range(n):
    T, P = list(map(int, input().split()))
    t.append(T)
    p.append(P)

for i in range(0, n):
    if t[i] <= n - i:
        dp[i + t[i]] = max(dp[i + t[i]], dp[i] + p[i])

    dp[i + 1] = max(dp[i + 1], dp[i])

print(dp[n])
