# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWRuoqCKkE0DFAXt&categoryId=AWRuoqCKkE0DFAXt&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=30&pageIndex=2

import sys
from tabnanny import check
from turtle import st
sys.stdin = open("//Users/yuyeong/Desktop/KEEP STUDYING/SW/4698_테니스의 특별한 소수.txt")

# 에라토스테네스의 체!
n = 10**6

def set_prime():
    for i in range(n):
        if prime[i] == 1:
            for j in range(i*2, n+1 ,i):
                prime[j] = 0
    
prime = [1]*(n+1)
prime[0], prime[1] = 0, 0
set_prime()

t = int(input())
for tc in range(1, t+1):
    d, a, b = map(int, input().split())
    result=[]
    for i in range(a, b+1):
        if str(d) in str(i) and prime[i]:
            result.append(i)
    
    print("#{} {}".format(tc,len(result)))