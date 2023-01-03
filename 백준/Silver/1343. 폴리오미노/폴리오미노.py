n = input().split('.')
n_str = ''

for i in n:
    # 홀수면 덮을 수 없음
    if len(i) % 2 == 1:
        print(-1)
        break
        # 4보다 크면 AAAA 덮기 
    while len(i) >= 4:
        n_str +='AAAA'
        i = i[4:]
        # 2가 남았으면 BB 덮기
    if len(i) == 2:
        n_str +='BB'
        i = i[2:]
    n_str +='.'
    
else:
    print(n_str[:-1])