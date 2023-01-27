# https://www.acmicpc.net/problem/9935


n = input()
m = list(input())

stack = []

for i in range(len(n)):
    # 스택에 하나씩 추가
    stack.append(n[i])
    # 스택의 마지막이 m 문자열과 같으면 삭제
    # print(stack[-len(m) :])
    if stack[-len(m) :] == m:
        del stack[-len(m) :]

if stack:
    print("".join(stack))
else:
    print("FRULA")
