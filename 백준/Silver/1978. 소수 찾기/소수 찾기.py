import sys
input = sys.stdin.readline

p = 10 ** 3
prime = [False, False] + [True] * (p - 1)

for i in range(1, p + 1):
    if prime[i]:
        for j in range(2 * i, p + 1, i):
            prime[j] = False 
n = int(input())
nums = list(map(int, input().split()))

cnt = 0

for num in nums:
    if prime[num]:
        cnt += 1

print(cnt)