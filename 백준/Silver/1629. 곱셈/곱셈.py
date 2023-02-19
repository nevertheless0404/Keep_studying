import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def dac(a, b):
    if b == 1:
        return a % C
    
    temp = dac(a, b // 2)
    
    if b % 2 == 0:
        return temp * temp % C
    
    else:
        return temp * temp * a % C
    
print(dac(A, B))