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
        if word[i - 1] == "(":
            stack.pop()
            # 들어가 있는 가로의 길이를 구해주고
            # 그 만큼 더해준당!
            ans += len(stack)
        else:
            # 그것이 아니면!
            # 그냥 하나만 더해줘!
            stack.pop()
            ans += 1
print(ans)
