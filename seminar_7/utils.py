def is_prime(n):
    for i in range (2, int(n/2+1)):
        if n % i == 0:
            return False 
        else:
            continue
    return True 
