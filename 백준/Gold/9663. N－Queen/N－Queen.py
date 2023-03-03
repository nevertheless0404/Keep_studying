import sys 
input = sys.stdin.readline

n = int(input())
row = [0] * n
result = 0 


def promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False        
    return True
    
def queens(x):
    global result 
    
    if x == n:
        result += 1
        return

    for i in range(n):
        row[x] = i
        if promising(x):
            queens(x + 1)

queens(0)
print(result)
