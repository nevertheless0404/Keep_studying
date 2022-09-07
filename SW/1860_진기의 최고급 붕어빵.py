# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LsaaqDzYDFAXc&categoryId=AV5LsaaqDzYDFAXc&categoryType=CODE&problemTitle=1860&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

import sys
sys.stdin = open("/Users/yuyeong/Desktop/KEEP STUDYING/SW/1860_진기의 최고급 붕어빵.txt")

t = int(input())
for tc in range(1, t+1):
    n, m, k = map(int, input().split())
    customer = list(map(int, input().split()))
    customer.sort()
    
    result = "possible"

    for i in range(n):
        # customer[i]초 까지 만들어진 붕어빵의 개수
        # 이전까지의 손님들에게 붕어빵 판것을 i+1로 해준 뒤
        # 빼준다!
        cnt = (customer[i] // m) * k - (i+1)
        # 만약 붕어빵의 개수가 0 미만이라면 
        # impossible
        if cnt < 0:
            result = "impossible"
            break
    print ('#%d %s'%(tc, result))
