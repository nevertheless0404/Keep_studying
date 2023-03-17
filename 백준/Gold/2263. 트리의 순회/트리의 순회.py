import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def find_preorder(l_in, r_in, l_post, r_post):
    # 재귀 탈출!
    if l_in > r_in or l_post > r_post:
        return 
    
    parent = post_order[r_post]
    print(parent, end=" ")

    split_idx = idx[parent]
    left = split_idx - l_in

    # 왼쪽 트리 
    find_preorder(l_in, split_idx - 1, l_post, (l_post + left) - 1)
    # 오른쪽 트리 
    find_preorder(split_idx + 1, r_in, l_post + left, r_post - 1)

n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

# 인덱스 번호 저장 
idx = [0] * (n + 1)
for i in range(n):
    idx[in_order[i]] = i

find_preorder(0, n - 1, 0, n - 1)