import sys 
from heapq import heappop, heapify

input = sys.stdin.readline

import heapq

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [i for i in range(v+1)]
edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

# heaify 리스트 내부의 원소들의 위에서 다룬 힙 구조에 맞게 재배치 
heapify(edges)

total_weight = 0
while edges:
    weight, a, b = heappop(edges)
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total_weight += weight

print(total_weight)