import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())
target = list(map(int, input().split()))


def bin(target):
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2
        if n_list[mid] == target:
            return True
        
        if target < n_list[mid]:
            right = mid - 1
        
        elif target > n_list[mid]:
            left = mid + 1

for i in range(m):
    if bin(target[i]):
        print(1)
    else:
        print(0) 