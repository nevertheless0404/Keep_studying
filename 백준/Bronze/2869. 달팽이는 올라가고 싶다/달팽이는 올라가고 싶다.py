a, b, c = map(int, input().split())
i = (c - b) / (a - b)
print(int(i) if i == int(i) else int(i) + 1) 