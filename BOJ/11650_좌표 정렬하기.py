# https://www.acmicpc.net/problem/11650

import sys
input = sys.stdin.readline

n = int(input())
num = []

for i in range(n):
    num.append(list(map(int, input().split())))
# 첫번째 인자 X줄부터 정렬, 그 다름 y인자 정렬
num.sort(key=lambda x:(x[0], x[1]))

for i in num:
    print(i[0], i[1])