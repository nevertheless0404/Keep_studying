# https://www.acmicpc.net/problem/4375

import sys
sys.stdin = open("/Users/yuyeong/Desktop/KEEP STUDYING/BOJ/4375_1.txt")

while True:
    try:
        n = int(input())
    except:
        break
    num = 0
    i = 1

    while True:
        # 10을 곱하고 1을 더해줌
        # num = 0 * 10 + 1 >> num 1
        # num = 1 * 10 + 1 >> num 11
        num = num*10 + 1
        # n==3, i ==1, num == 0
        # num == 0*10+1 == 1
        # 1 %= 3 >> num== 1
        # if num!=0이므로 i +=1 >> i == 2
        # - num == 1*10+1 == 11
        # 11%=3 >> num== 2
        # if num!=0이므로 i +=1 >> i == 3
        # - num == 2*10+1 == 21
        # 21%=3 >> num==0
        # if num==0이므로 print i == 3, break
        num % n
        if num == 0:
            print(i)
            break
        i +=1
