import sys 
input = sys.stdin.readline

n = int(input().strip())

stack = []
for i in range(n):
    cmd = input().strip().split()
    if cmd[0] == 'push':
        stack.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(stack) != 0:
            print(stack.pop(0))
            
        else:
            print(-1)
            
    elif cmd[0] == 'size':
        print(len(stack))
        
    elif cmd[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if len(stack) != 0:
            print(stack[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)