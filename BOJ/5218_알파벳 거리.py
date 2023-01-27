# https://www.acmicpc.net/problem/5218

import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    a, b = input().split()
    print("Distances:", end=" ")

    for i in range(len(a)):
        if ord(a[i]) <= ord(b[i]):
            print(ord(b[i]) - ord(a[i]), end=" ")

        else:
            print(ord(b[i]) - ord(a[i]) + 26, end=" ")

    print()
