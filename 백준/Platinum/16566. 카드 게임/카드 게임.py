import sys 
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 8)

def find(v):
    if v == card[v]:
        return v
    card[v] = find(card[v])
    return card[v]


def union(v1, v2):
    n1 = find(v1)
    n2 = find(v2)
    card[n1] = n2
    
def upper(key):
    i, j = 0, m - 1
    while i <= j:
        mid = (i + j) // 2
        if min[mid] <= key:
            i = mid + 1
        else:
            j = mid - 1
    
    return i    
    
n, m, k = map(int, input().split())

min = list(map(int, input().split()))
card = [i for i in range(m + 1)]
soo = list(map(int, input().split()))
min.sort()

for num in soo:
    idx = upper(num)
    select_idx = find(idx)
    print(min[select_idx])
    union(select_idx, select_idx + 1)