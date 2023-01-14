def k_num(n,k):
    if k == 10:
        return n
    else:
        new_n = ""
        while n > 0:
            new_n += str(n % k)
            n = n // k
        return new_n[::-1]

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**(1/2)+1)):
        if n % i == 0:
            return False
    return True
    
def solution(n, k):
    answer = 0
    num = k_num(n,k)
    nums = str(num).split("0")
    for x in nums:
    	#x가 비어있는 경우를 예외처리 한다
        if x and isPrime(int(x)):
            answer += 1
    return answer