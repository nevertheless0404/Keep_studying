# https://www.acmicpc.net/problem/2302

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
vip = [int(input()) for _ in range(m)]

dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

result = 1
if m >= 1:
    tmp = 0
    # 좌석의 개수에 따라 경우의 수를 구하면 vip 유무에 따라 경우의 수를 곱함
    for i in range(m):
        result *= dp[vip[i] - 1 - tmp]
        tmp = vip[i]
    result *= dp[n - tmp]
else:
    result = dp[n]
print(result)
