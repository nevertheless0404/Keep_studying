# https://www.acmicpc.net/problem/1715

# 1. 카드숫자 들이 들어간 리스트가 있어야함 (힙이라는 자료구조를 가진 리스트)
# 2. 합 한것을 누적 합으로 넣어줄 변수가 필요하다.
# 3. 힙을 이용해서 최솟값만 두개를 뽑아서 합을 해준다
# 4. 합한 친구를 다시 힙 안으로 넣어준다
# 5. 언제까지 3~5번 과정을 진행할것인가? -> 힙 이라는 자료구조를 가진 리스트의 길이가 1이 될때까지.

import heapq
n = int(input())

card = []
for _ in range(n):
    heapq.heappush(card, int(input()))
ans = 0

while len(card) != 1:
    first = heapq.heappop(card)
    second = heapq.heappop(card)

    hao = first + second
    ans += hao
    heapq.heappush(card, hao)
print(ans)