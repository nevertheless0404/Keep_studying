# https://www.acmicpc.net/problem/16120

import sys

input = sys.stdin.readline

p = input()
stack = []


for i in range(len(p)):
    stack.append(p[i])
    if stack[-1] == "P" and stack[-4:] == list("PPAP"):
        del stack[-4:]
        stack.append("P")

if stack == list("PPAP") or stack == list("P"):
    print("PPAP")
else:
    print("NP")
