# 충족가능성 문제 여러 개의 boolean 변수들로 이루어진 boolean expression이 있을때,
# 각 변수의 값을 true, false 중 하나로 설정하여 전체 식의 결과를 true로 만들 수 있냐는 문제


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

n, m = map(int, input().split())
# 그래프 생성
graph = [[] for _ in range(2 * n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[-a].append(b)
    graph[-b].append(a)
    
scc_num = 1
index = 1
stack = []
scc_index = [0] * (2 * n + 1)
check = [0] * (2 * n + 1)
visit = [0] * (2 * n + 1)

def SCC(node):
    global index, scc_num
    visit[node] = index
    # 방문 순서 기록
    root = index
    index += 1
    stack.append(node)
    
    # 인접한 정점들에 대해 재귀적으로 탐색
    for i in graph[node]:
        if not visit[i]:
            root = min(root, SCC(i))
        elif not check[i]:
            root = min(root, visit[i])
            
    # SCC를 찾았을 때
    if root == visit[node]: 
        # 스택에서 노드를 꺼내며 SCC의 일부로 체크하고 SCC 번호 부여
        while stack:
            t = stack.pop()
            check[t] = 1
            scc_index[t] = scc_num
            if node == t:
                break
        scc_num += 1
        
    return root


for j in range(1, n + 1):
    if not visit[j]:
        SCC(j)

is_possible = True
for j in range(1, n + 1):
    if scc_index[j] == scc_index[-j]:
        is_possible = False
        break

if is_possible:
    print(1)
else:
    print(0)