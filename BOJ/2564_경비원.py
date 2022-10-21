# https://www.acmicpc.net/problem/2564

import sys

input = sys.stdin.readline


def Dong(loc, dist):
    if loc == 1:
        return dist
    elif loc == 4:
        return w + dist
    elif loc == 2:
        return w + h + w - dist
    elif loc == 3:
        return w + h + w + h - dist


w, h = map(int, input().split())

num = int(input())

store = [0] * (num + 1)

dist_list = []

for i in range(num + 1):
    loc, dist = map(int, input().split())
    dist_list.append(Dong(loc, dist))

# 동근이의 0에서부터 떨어진 위치를 저장
dong_dist = dist_list[-1]

result = 0
for i in range(num):
    distance = abs(dist_list[i] - dong_dist)

    # 전체 길이를 구해준다.
    total = 2 * (w + h)

    result += min(distance, total - distance)

print(result)
