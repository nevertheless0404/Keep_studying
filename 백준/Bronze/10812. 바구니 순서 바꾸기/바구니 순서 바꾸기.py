n, m = map(int, input().split())
box = [i + 1 for i in range(n)]
for _ in range(m):
    i, j , k = map(int, input().split())
    box = box[:i - 1] + box[k - 1 : j] + box[i - 1:k - 1] + box[j:]
for a in box:
    print(a, end=" ")