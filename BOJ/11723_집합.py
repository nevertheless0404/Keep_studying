# add = or |
# remove = and &
# check = and &
# toggle = xor |
# all = not ~


import sys

m = int(sys.stdin.readline())

num = 0
for i in range(m):
    com = sys.stdin.readline().rstrip().split()

    if com[0] == "all":
        num = (1 << 20) - 1

    elif com[0] == "empty":
        num = 0

    else:
        option = com[0]
        bit = int(com[1]) - 1

        if option == "add":
            num |= 1 << bit

        elif option == "remove":
            num &= ~(1 << bit)

        elif option == "check":
            if num & (1 << bit) == 0:
                print(0)
            else:
                print(1)
        elif option == "toggle":
            num = num ^ (1 << bit)

