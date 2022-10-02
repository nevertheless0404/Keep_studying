# https://www.acmicpc.net/problem/11651

import sys

input = sys.stdin.readline

n = int(input())
nums = []

for _ in range(n):
    x, y = map(int, input().split())
    nums.append([x, y])

nums.sort(key=lambda x: (x[1], x[0]))

for i in nums:
    print(i[0], i[1])
