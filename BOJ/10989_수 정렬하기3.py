# https://www.acmicpc.net/problem/10989

import sys
input = sys.stdin.readline

n = int(input())
nums = [0]*10001

for i in range(n):
    nums[int(sys.stdin.readline())] +=1

for i in range(10001):
    if nums[i] != 0:
        for j in range(nums[i]):
            print(i)