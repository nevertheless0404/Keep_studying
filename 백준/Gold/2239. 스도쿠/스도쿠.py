import sys
input = sys.stdin.readline

# 행 체크
def row_check(r, num):
    for c in range(9):
        if board[r][c] == num:
            return False
    return True

# 열 체크
def col_check(c, num):
    for r in range(9):
        if board[r][c] == num:
            return False
    return True

# 3 * 3 체크
def three_check(r, c, num):
    nr = (r // 3) * 3
    nc = (c // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[nr + i][nc + j] == num:
                return False
    return True

def dfs(depth):
    if depth == len(zero):
        for row in range(9):
            for col in range(9):
                print(board[row][col], end="")
            print()
        exit()
    
    nr, nc = zero[depth]
    for num in range(1, 10):
    	# 세 가지 조건에 모두 만족하면 숫자 그리기
        if row_check(nr, num) and col_check(nc, num) and three_check(nr, nc, num):
            board[nr][nc] = num
            dfs(depth + 1)
            board[nr][nc] = 0

board = []
zero = []		
for r in range(9):
    board.append(list(map(int, input().rstrip())))
    for c in range(9):
        if board[r][c] == 0:
            zero.append((r, c))
dfs(0)