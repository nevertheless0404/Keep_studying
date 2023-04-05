import sys 
input = sys.stdin.readline

n = int(input())

# 에라토스테네스의 체 
primeList = []
array = [False, False] + [True] * (n - 1)

for i in range(2, n + 1):
    if array[i]:
        primeList.append(i)
    
    for j in range(i * i, n + 1, i):
        array[j] = False


# 투 포인터 
interval_sum = 0
end = 0 
cnt = 0
start = 0

while True:
    if interval_sum >= n:
        if interval_sum == n:
            cnt += 1
        interval_sum -= primeList[start]
        start += 1
    
    elif end == len(primeList):
        break
    else:
        interval_sum += primeList[end]
        end += 1

print(cnt)