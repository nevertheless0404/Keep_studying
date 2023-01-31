def solution(chicken):
    answer = 0
    coupon = chicken 
    
    while coupon >= 10:
        ate = coupon // 10
        answer += ate
        coupon = coupon % 10 + ate
    return answer