def solution(n, lost, reserve):
    
    reserve_n = set(reserve) - set(lost)
    lost_n = set(lost) - set(reserve)
    
    for i in reserve_n:
        if i - 1 in lost_n:
            lost_n.remove(i - 1)
        
        elif i + 1 in lost_n:
            lost_n.remove(i + 1)
            
    answer = n-len(lost_n)
    
    return answer