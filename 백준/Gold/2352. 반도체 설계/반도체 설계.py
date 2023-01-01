import sys
input = sys.stdin.readline
from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
dp = []

for i in a:
    k = bisect_left(dp, i)
    if len(dp) <= k:
        dp.append(i)
    else:
        dp[k] = i
print(len(dp))