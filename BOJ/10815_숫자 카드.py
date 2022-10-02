# https://www.acmicpc.net/problem/10815


import sys

input = sys.stdin.readline

n = int(input())
n_arr = sorted(list(map(int, input().split())))
m = int(input())
m_arr = list(map(int, input().split()))

for i in m_arr:
    answer = 0
    left = 0
    right = len(n_arr) - 1
    while left < right:
        mid = (left + right) // 2
        if n_arr[mid] > i:
            right = mid - 1
        elif n_arr[mid] < i:
            left = mid + 1
        else:
            answer = 1
            break
    print(answer, end=" ")
