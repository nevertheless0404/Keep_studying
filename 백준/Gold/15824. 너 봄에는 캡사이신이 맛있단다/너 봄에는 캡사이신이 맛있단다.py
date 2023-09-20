import sys 
input = sys.stdin.readline
MOD = 1000000007

n = int(input())
arr = sorted(list(map(int, input().split())))
result = 0

for i in range(n):
    result += arr[i]*(pow(2, i, MOD)-pow(2, n-i-1,MOD))
    
print(result%MOD)
    


