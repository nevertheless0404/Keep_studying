# https://www.acmicpc.net/problem/2504

# import sys

# input = sys.stdin.readline

bracket = list(input())
stack = []
tmp = 1
result = 0

# tmp를 괄호 시작할 때 곱해주고 닫힌 가로는 만났을 때
# tmp를 result 로 넣고 나눠 주기
for i in range(len(bracket)):

    if bracket[i] == "(":
        stack.append(bracket[i])
        tmp *= 2

    elif bracket[i] == "[":
        stack.append(bracket[i])
        tmp *= 3

    elif bracket[i] == ")":
        if not stack or stack[-1] == "[":
            result = 0
            break
        if bracket[i - 1] == "(":
            result += tmp
        stack.pop()
        tmp //= 2

    else:
        if not stack or stack[-1] == "(":
            result = 0
            break
        if bracket[i - 1] == "[":
            result += tmp

        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(result)
