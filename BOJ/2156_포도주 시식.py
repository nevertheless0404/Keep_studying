# https://www.acmicpc.net/problem/2156

import sys

input = sys.stdin.readline

n = int(input())
wine = [int(input()) for _ in range(n)]

dp = [0, wine[0]]

if n > 1:
    dp.append(wine[0] + wine[1])

for i in range(3, n + 1):
    dp.append(
        max(dp[i - 2] + wine[i - 1], dp[i - 1], dp[i - 3] + wine[i - 1] + wine[i - 2])
    )

print(dp[n])
