import math

def check_prime(num):
    num = int(num)
    if num == 2:
        return True
    elif num < 2:
        return False
    else:
        for i in range(2, math.ceil(math.sqrt(num)+1)):
            if num % i == 0:
                return False
        return True
            
def get_factors(num, include_1=True, sorted=False):
    factors = [1, num] if include_1 == True else []
    for i in range(2, math.ceil(math.sqrt(num))):
        if num % i == 0 and i not in factors:
            factors.append(i)
            factors.append(int(num/i))
    if sorted == True:
        factors.sort()
    return factors
