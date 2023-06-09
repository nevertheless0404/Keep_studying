while True:
    n = input()
    
    if n == "0":
        break
    
    result = "no"
    
    if n == n[::-1]:
        result = "yes"
        
    print(result)