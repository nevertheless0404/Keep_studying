# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

import sys
sys.stdin = open("/Users/yuyeong/Desktop/TIL/KEEP STUDYING/SW/4836_색칠하기.txt")


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    result = [[0] * 10 for _ in range(10)]

    for n in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                # 같은 색깔은 덧칠하지 않는다고 했으므로,
                # 색깔 영역이 이미 같은 숫자로 채워지면 continue
                if result[i][j] == color:
                    continue
                result[i][j] += color

    cnt = 0
    for x in range(len(result)):
        for y in range(len(result[x])):
            # 값이 보라색이면 카운트 
            if result[x][y] >= 3:
                cnt += 1

    print(f'#{t} {cnt}')
