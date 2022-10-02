# https://www.acmicpc.net/problem/10799

from inspect import stack
import sys

input = sys.stdin.readline

word = input().rstrip()
stack = []
ans = 0

for i in range(len(word)):
    if word[i] == "(":
        stack.append(word[i])

    else:
        # ')'가 나고 이전 문가 '(' 이었다면
        # 레이저가 쏜다!
        # 현재  쌓인 '(' 개수 (쇠막대기 개수)만큼 개수를 더해준다.
        if word[i - 1] == "(":
            stack.pop()
            ans += len(stack)
        else:
            # 그것이 아니면!
            # 그냥 하나만 더해줘!
            stack.pop()
            ans += 1
print(ans)
