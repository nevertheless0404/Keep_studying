import sys 
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

q = []
tmp = []

for i in a :
    if not q or i > q[-1]:
        q.append(i)
        tmp.append((len(q) - 1, i))

    else:
        # index를 찾은 후 그 값을 x로 변경
        q[bisect_left(q, i)] = i
        tmp.append((bisect_left(q, i), i))


result = []
last_idx = len(q) - 1

# 역순으로 검사 
for j in range(len(tmp)-1, -1, -1):
    if tmp[j][0] == last_idx:
        result.append(tmp[j][1])
        # 한 단계 낮춤
        last_idx -= 1

print(len(result))
# 뒤집어서 출력 
print(*reversed(result))