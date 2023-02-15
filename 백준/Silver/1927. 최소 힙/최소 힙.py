import sys
from heapq import heappop, heappush 
input = sys.stdin.readline

n = int(sys.stdin.readline())
heap=[]

for i in range(n):   
    x = int(input())
    
    if x != 0:
        heappush(heap,x)
    else:
        if len(heap) != 0:
            print(heappop(heap))
        else:
            print(0)