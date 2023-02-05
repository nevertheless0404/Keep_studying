# https://www.acmicpc.net/problem/15486

import sys

input = sys.stdin.readline

n = int(input())

t = []
p = []
dp = [0] * (n + 1)

# n일부터 거꾸로 시작하여 받을 수 있는 최대 금액
for _ in range(n):
    T, P = list(map(int, input().split()))
    t.append(T)
    p.append(P)

# dp[i]를 n일부터 i일까지 받을 수 있는 최대 상담 금액 
for i in range(0, n):
    if t[i] <= n - i:
        dp[i + t[i]] = max(dp[i + t[i]], dp[i] + p[i])

    dp[i + 1] = max(dp[i + 1], dp[i])

print(dp[n])
