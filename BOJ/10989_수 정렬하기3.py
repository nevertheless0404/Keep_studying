# https://www.acmicpc.net/problem/10989

import sys
input = sys.stdin.readline

n = int(input())
nums = [0]*10001
# O(n) 정렬 알고리즘
# ex) 3이 2번 등장: 3의 인덱스는 2
# ex) 7이 1번 등장: 7의 인덱스는 1
# 앞에서부터 진행해서 수 하나씩 등장할 때마다 인덱스를 하나씩 증가

for i in range(n):
    nums[int(sys.stdin.readline())] +=1

for i in range(10001):
    if nums[i] != 0:
        for j in range(nums[i]):
            print(i)