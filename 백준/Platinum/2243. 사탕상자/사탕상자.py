import sys 
input = sys.stdin.readline

def putcandy(left, right, node, t, c):
    tree[node] += c
    if left == right:
        return
    mid = (left + right) // 2
    # 왼쪽 구간에 맛이 포함
    if t <= mid:
        putcandy(left, mid, node*2, t, c)
    # 오른쪽 구간
    else:
        putcandy(mid+1, right, node*2 + 1, t, c)
        

def findcandy(left, right, node, t):
    tree[node] -=1
    if left == right:
        return left
    mid = (left + right) // 2
    if tree[node * 2] >= t:
        return findcandy(left, mid, node * 2, t)
    
    else:
        return findcandy(mid+1, right, node*2+1, t-tree[node * 2])
      

n = int(input())
tree = [0] * (1000000 * 4)

for i in range(n):
    line = list(map(int, input().rstrip().split()))
    if len(line) == 2:
        t = line[1]
        print(findcandy(1, 10**6, 1, t))
        
    elif len(line) == 3:
        i, t, c = line
        putcandy(1, 10**6, 1, t, c)