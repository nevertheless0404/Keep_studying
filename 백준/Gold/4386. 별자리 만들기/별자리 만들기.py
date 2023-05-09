import sys 
import math
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
        
    return parent[x]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
        
n = int(input())
parent = [i for i in range(n + 1)]

stars = []
ed = []
result = 0

for _ in range(n):
    x, y = map(float, input().split())
    stars.append((x, y))
    
for i in range(n - 1):
    for j in range(i + 1, n):
        ed.append((math.sqrt((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2), i, j))
ed.sort()

for e in ed:
    cost, x, y = e
    
    if find_parent(x) != find_parent(y):
        union(x, y)
        result += cost
        
print(round(result, 2))