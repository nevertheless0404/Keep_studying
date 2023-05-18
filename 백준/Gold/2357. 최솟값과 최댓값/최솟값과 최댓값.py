import math
import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

def tree(idx, start, end):
    # 리프 노드 
    if start == end:
        # 최소, 최대값 동일
        s[idx] = (arr[start], arr[start])
        return s[idx]
    
    mid = (start + end) // 2
    
    left = tree(idx * 2, start, mid)
    right = tree(idx * 2 + 1, mid + 1, end)
    
    # 각각 최소, 최대값 계산 
    s[idx] = (min(left[0], right[0]), max(left[1], right[1]))
    
    return s[idx]
    
def find(idx, start, end):
    if range2 < start or range1 > end:
        return(10**9+1, 0)
    
    if range1 <= start and end <= range2:
        return s[idx]
    
    mid = (start + end) // 2
    left =  find(idx * 2, start, mid)
    right = find(idx * 2 + 1, mid + 1, end)
    return (min(left[0], right[0]), max(left[1], right[1]))

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)] # 이런 방식으로 입력받을 수 있다니

h = math.ceil(math.log2(n)) + 1 # 노드 개수에 따른 트리의 높이 계산 공식
nodeNum = 1 << h ## 2^h 계산
s = [0 for _ in range(nodeNum)]
tree(1, 0, len(arr) - 1)

for _ in range(m):
    range1, range2 = map(int, input().split())
    range1, range2 = range1 - 1, range2 - 1 # index이므로 -1 해주기
    result = find(1, 0, len(arr) - 1)
    print(result[0], result[1])