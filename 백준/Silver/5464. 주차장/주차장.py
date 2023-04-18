import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

fare = [0]
for _ in range(n):
    fare.append(int(input()))
    
    
weight = [0]
for _ in range(m):
    weight.append(int(input()))
    
enter = []
for _ in range(2 * m):
    enter.append(int(input()))
    
queue = deque(enter)

parking = [[True, 0] for _ in range(n + 1)]

result = 0 
wait = deque([])
while queue:
    car = queue.popleft()
    wait_q = True
    if car > 0 :
        for i in range(1, n + 1):
            if parking[i][0] == True:
                result += weight[car] * fare[i]
                parking[i][1] = car
                parking[i][0] = False
                wait_q = False
                break
            
        if wait_q:
            wait.append(car)
            
    else:
        car = -car
        
        for i in range(1, n + 1):
            if parking[i][1] == car:
                parking[i][0] = True
                if len(wait) != 0:
                    car = wait.popleft()
                    parking[i][0] = False
                    parking[i][1] = car
                    result += weight[car] * fare[i]
                break

print(result)