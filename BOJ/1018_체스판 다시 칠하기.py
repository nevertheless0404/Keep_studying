# https://www.acmicpc.net/problem/1018

import sys
sys.stdin = open("/Users/yuyeong/Desktop/KEEP STUDYING/BOJ/1018_체스판 다시 칠하기.txt")

n,m=map(int,input().split())

chess=[]
cnt=[]
for i in range(n):
    chess.append(input())

#8*8로 자르기 위해, -7해준다
for a in range(n-7):
    for b in range(m-7):
        w_index=0 #흰색으로 시작
        b_index=0 #검은색으로 시작
        # 시작지점
        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i+j)%2==0:
                    if chess[i][j]!='W':
                        # w로 칠하는 갯수
                        w_index+=1
                    else:#W일 때
                        b_index+=1
                else:
                    if chess[i][j]!='W':
                        b_index+=1
                    else:
                        w_index+=1
                        
        cnt.append(w_index) #W로 시작할 때 경우의 수
        cnt.append(b_index) #B로 시작할 때 경우의 수
print(min(cnt))