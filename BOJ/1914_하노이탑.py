# https://www.acmicpc.net/problem/1914

import sys
sys.stdin = open("/Users/yuyeong/Desktop/KEEP STUDYING/BOJ/1914_하노이탑.txt")


def hanoi(n, a, b, c):  # 사용자 정의 함수
    if n == 1:
        print(a,c, sep=' ')
    else:
        hanoi(n-1, a, c, b)  # 첫 번째 장대에서 두 번째 장대로!
        hanoi(1, a, b, c)  # 첫 번째 장대에서 가장 큰 원판을 세 번째 장대로!
        hanoi(n-1, b, a, c)  #  두 번째 장대에서 세 번째 장대로

n = int(input())
print(2**n-1)  # 원판의 이동 횟수
if n <= 20:
    hanoi(n, 1, 2, 3)