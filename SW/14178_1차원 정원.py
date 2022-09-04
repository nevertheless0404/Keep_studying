# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AX_N3oSqcyUDFARi&categoryId=AX_N3oSqcyUDFARi&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

import sys
sys.stdin = open("/Users/yuyeong/Desktop/KEEP STUDYING/SW/14178_1차원 정원.txt")

t = int(input())
for tc in range(1, t+1):
    n, d = map(int, input().split())
    d = d*2+1
    # 나눈값을 할당
    result = n//d
    if n % d != 0:
        result += 1
    
    print("#%d %d" % (tc, result))