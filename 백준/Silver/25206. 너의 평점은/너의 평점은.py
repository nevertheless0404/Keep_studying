import sys 
input = sys.stdin.readline

score = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
         'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

result = 0
total = 0

for _ in range(20):
    a, b, c = input().split()
    b = float(b)
    if c != 'P':
        result += b
        total += b * score[c]

print('%.6f' % (total / result))