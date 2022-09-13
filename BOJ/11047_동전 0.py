# https://www.acmicpc.net/problem/11047

import sys
sys.stdin = open("/Users/yuyeong/Desktop/KEEP STUDYING/BOJ/11047_동전 0.txt")

n, k = map(int, input().split())
coin = []
cnt = 0

for _ in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)


for i in coin:
    cnt += k//i
    k = k%i
print(cnt)