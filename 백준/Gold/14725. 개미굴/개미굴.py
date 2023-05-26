import sys 
input = sys.stdin.readline

n = int(input())
food = []
for i in range(n):
    data = list(input().split())
    food.append(data[1:])
    
food.sort()

dash = '--'
reault = []

for i in range(n):
    # 중복 없이 그대로 출력 
    if i == 0:
        for j in range(len(food[i])):
            reault.append(dash * j + food[i][j])
            
    else:
        list_num = 0 
        for j in range(len(food[i])):
            if food[i - 1][j] != food[i][j] or len(food[i - 1]) <= j:
                break
            else:
                list_num = j + 1
                
        for j in range(list_num, len(food[i])):
            reault.append(dash * j + food[i][j])
            
for k in reault:
    print(k)