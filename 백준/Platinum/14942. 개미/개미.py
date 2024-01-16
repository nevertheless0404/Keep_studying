import sys 
input = sys.stdin.readline

n = int(input())

ant = [0]
room = [[i] for i in range(n + 1)]
position = [i for i in range(n + 1)]

for _ in range(n):
    ant.append(int(input()))
    
tunnel = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, l = map(int, input().split())
    
    tunnel[a].append((b, l,))
    tunnel[b].append((a, l,))
    
visit = [1]
visited = [False for _ in range(n + 1)]
stack = []

next = []

while visit:
    now = visit.pop()
    
    # 만약에 음수라면 노드를 다 돌고 돌아옴
    back = False
    if now < 0:
       back = True
       now = - now
       
    # 방문 했는지 확인 
    if now == 1 and visited[1]:
        while next:
            room[now].append(next[-1])
            position[next.pop()] = now        
        continue
    
    if visited[now]:
        while next:
            room[now].append(next[-1])
            position[next.pop()] = now
            
        if back:
            cost = stack.pop()
            
            # 개미들을 다음방으로 
            for i in room[now]:
                ant[i] -= cost
                if ant[i]>= 0:
                    next.append(i)
                    
        continue
    
    visited[now] = True
    
    
    visit.append(-now)
    
    for room_k, cost in tunnel[now]:
        if visited[room_k]:
            continue
        
        visit.append(room_k)
        visit.append(now)
        stack.append(cost)         
    
    
for i in range(1, n + 1):
    print(position[i])