change = [25, 10, 5, 1]
t = int(input())

for _ in range(t):
    c = int(input())
    result = []
    
    for i in change:
        result.append(c//i)
        c = c % i
    print(*result)