# https://www.acmicpc.net/problem/1107

import sys

sys.stdin = open("/Users/yuyeong/Desktop/무제 폴더 2/BOJ/1107_리모콘.txt")

n = int(input())
m = int(input())
broken = list(map(str, input().split()))
# 리모컨을 눌러야 하는 최대 갯수
cnt = abs(100 - n)

# 반복문을 통해 이동해야하는 채널로 가기
for i in range(1000001):

    # 반복문을 통해 채널로 이동하기 위해 눌러야 하는 번호가 고장났는지 확인
    for j in str(i):
        if j in broken:
            break

    # 채널로 이동 가능하다면 원래 cnt와 채널을 누른 개수와 +/- 를 누른 개수를 cnt에 담는다.
    else:
        cnt = min(cnt, len(str(i)) + abs(i - n))
print(cnt)
