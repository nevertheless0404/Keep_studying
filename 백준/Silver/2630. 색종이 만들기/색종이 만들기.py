import sys

input = sys.stdin.readline

N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]

blue = 0
white = 0

def color(x, y, N):
    global blue, white
    color_paper = array[x][y]
    # 네모 전체를 봐야하기 때문에
    for i in range(x, x + N):
        for j in range(y, y + N):
            # 하나라도 같은 색이 아니라면
            if color_paper != array[i][j]:
                # 4등분
                color(x, y, N // 2)  # 1사분면
                color(x, y + N // 2, N // 2)  # 2사분면
                color(x + N // 2, y, N // 2)  # 3사분면
                color(x + N // 2, y + N // 2, N // 2)  # 4사분면
                return

    if color_paper == 0:
        white += 1
        return
    else:
        blue += 1
        return


color(0, 0, N)
print(white)
print(blue)