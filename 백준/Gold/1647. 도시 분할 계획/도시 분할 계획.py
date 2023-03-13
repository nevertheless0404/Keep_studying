import sys
input = sys.stdin.readline

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
edge = []
result = 0

for i in range(m):
    a, b, c = map(int, input().split())
    edge.append((a, b, c))

edge.sort(key=lambda x : x[2])

for i in range(1, n + 1):
    parent[i] = i

for i in edge:
    a, b, c = i
    if find(a) != find(b):
        union(a, b)
        result += c
        last = c

print(result - last)