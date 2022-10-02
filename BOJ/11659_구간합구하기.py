# https://www.acmicpc.net/problem/11659

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums_add = [0]

for i in range(n):
    # 누적합 생성
    nums_add.append(nums_add[-1] + nums[i])

for _ in range(m):
    i, j = map(int, input().split())

    if i == 1:
        print(nums_add[j])
    else:
        print(nums_add[j] - nums_add[i - 1])
