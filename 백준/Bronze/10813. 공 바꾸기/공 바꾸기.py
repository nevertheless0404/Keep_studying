

n, m = map(int, input().split())
basket = [i for i in range(1, n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    tmp = basket[b - 1]
    basket[b - 1] = basket[a - 1]
    basket[a - 1] = tmp
    
print(*basket)