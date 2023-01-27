# https://www.acmicpc.net/problem/2749

import sys

input = sys.stdin.readline

n = int(input())

# n 번째 피보나치 수 1,000,000으로 나눈 나머지
mod = 1000000
# 피보나치 수 시작
fibo = [0, 1]
p = mod // 10 * 15

for i in range(2, p):
    fibo.append(fibo[i - 1] + fibo[i - 2])
    fibo[i] %= mod

# n번째 피보나치 수를 mod으로 나눈 나머지는 n%p번째 피보나치 수를
# mod을 나눈 나머지와 같다
print(fibo[n % p])
