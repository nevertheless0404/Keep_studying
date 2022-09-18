# https://www.acmicpc.net/problem/13458

import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int,input().split()))
b, c = map(int, input().split())
result = 0

for i in s:
    # 각 시험장에 있는 음시자수 - 총감독관이 감시 할 수 있는 수 
    i -= b
    # 총 감독관은 무조건 1명 !
    cnt = 1
    # 이제 부감독관을 구해보자
    # 부 감독관이 감시할 수 있는 응시자 수
    # 0명 초과, 응시자 수와 부감독관 나눠서 
    # 카운트 해주기 
    # 나머지가 0이 아니면 또 카운트 
    if i > 0:
        cnt += i//c
        if i % c != 0:
            cnt += 1
    result += cnt
print(result)
