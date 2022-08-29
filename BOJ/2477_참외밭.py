# https://www.acmicpc.net/problem/2477

import sys
sys.stdin = open("/Users/yuyeong/Desktop/TIL/KEEP STUDYING/BOJ/2477_참외밭.txt")

k = int(input())
pos = []
for i in range(6):
    # 반시계 반향으로 돌면서 6개의 변이 입력 
    # 순서대로 입력 됨! 
    dir, lenght = map(int, input().split())
    # 길이만 저장 
    pos.append(lenght)

big = 0
sma = 0
for i in range(6):
    # 한 칸씩 옮기면서 큰 직사각형 구하기
    tmp = pos[i] * pos[(i + 1) % 6]
    if big < tmp:
        big = tmp
        idx = i
# 가장 넓은 변에서 +3칸 + 4칸 을 이동하게 되면 
# 작은 사격형의 변의 길이를 구할 수 있음 
small = pos[(idx + 3) % 6] * pos[(idx + 4) % 6]
# 참외의 개수 * (큰 직사각형의 넓이 - 작은 직사각형의 넓이)
print(k * (big - small))