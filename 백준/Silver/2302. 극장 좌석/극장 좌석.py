import sys

input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
vip = [int(input()) for _ in range(m)]

dp = [0] * (41)
dp[0] = 1
dp[1] = 1
dp[2] = 2
# dp[3] = 3 # 1 2 3, 1 3 2, 2 1 3

# 점화식
for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

result = 1
first = 0

for i in range(m):
    last = vip[i]
    result *= dp[last - first - 1]
    first = last

result *= dp[n - first]
print(result)