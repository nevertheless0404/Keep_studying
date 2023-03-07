import sys
input = sys.stdin.readline

n = int(input())
tree = {}

for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]

# 전위순회 = 루트, 왼쪽, 오른쪽
def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

# 중위순회 = 왼쪽, 루트, 오른쪽
def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

# 후위순회 = 왼쪽, 오른쪽, 루트 
def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')