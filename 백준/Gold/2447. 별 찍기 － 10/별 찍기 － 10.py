n = int(input())

def star(n):
    if n == 3:
        return ['***', '* *', '***']
    
    stars = star(n//3)
    arr = []

    for i in stars:
        arr.append(i * 3)
    
    for i in stars:
        arr.append(i + ' '*(n//3) + i)

    for i in stars:
        arr.append(i * 3)
    
    return arr


print('\n'.join(star(n)))