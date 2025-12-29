def pow(x, n):

    if n == 0:
        return 1
    if x == 1:
        return 1
    
    # Recursive case
    t = pow(x, n // 2)  
    
    if n > 0:
        if n % 2 == 0:
            return t * t
        else:
            return t * t * x
    else:  # n < 0
        if n % 2 == 0:
            return 1 / (t * t)
        else:
            return 1 / (t * t * x)