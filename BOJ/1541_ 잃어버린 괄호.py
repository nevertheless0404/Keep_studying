# https://www.acmicpc.net/problem/1541

import sys

input = sys.stdin.readline

arr = input().split("-")
num = 0
for i in arr[0].split("+"):
    num += int(i)

for i in arr[1:]:
    for j in i.split("+"):
        num -= int(j)

print(num)
