# https://www.acmicpc.net/problem/12015

import sys 
input = sys.stdin.readline

# bisect은 바이너리 서치를 사용
# bisect_left(array, value)를 하게 되면 
# array에서 해당 value의 인덱스를 구하는데 왼쪽이 경계선 

from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
dp = [0]

for i in a:
    if dp[-1] < i:
        dp.append(i)

    else:
        dp[bisect_left(dp, i)] = i

print(len(dp) - 1)

