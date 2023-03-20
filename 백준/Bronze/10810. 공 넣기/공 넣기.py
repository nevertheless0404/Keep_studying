import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
arr = [0] * n 

for i in range(m):
    a, b, c = map(int, input().split())
    for j in range(a, b + 1, 1):
        arr[j - 1] = c
for i in range(n):
    print(arr[i],'',end='')