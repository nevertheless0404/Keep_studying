import sys 
input = sys.stdin.readline

n = int(input())
arr = [0] * 10
num = 1

def make_nine(n):
    while n % 10 != 9:
        for i in str(n):
            arr[int(i)] += num
        n -= 1
    return n

while n > 0:
    n = make_nine(n)
    if n < 10:
        for i in range(n + 1):
            arr[i] += num
            
    else:
        for i in range(10):
            arr[i] += (n // 10 + 1) * num
    arr[0] -= num
    num *= 10
    n //= 10

for i in range(0, 10):
    print(arr[i], end=" ")
        
    