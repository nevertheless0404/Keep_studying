import sys 
input = sys.stdin.readline 

n, m = map(int, input().split())
tmp = [i + 1 for i in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    tmp[a - 1:b] = tmp[a - 1:b][::-1]
    
print(*tmp)