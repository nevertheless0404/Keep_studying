while True:
    tc = list(map(int, input().split()))
    if tc[0] == 0 and tc[1] == 0 and tc[2] == 0:
        break
    tc.sort()
    # 피타고라스 정리
    if tc[2]**2 == tc[0]**2 + tc[1]**2:
        print('right')
    else:
        print('wrong')