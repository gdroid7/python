def checkPrime(no):
    
    if no < 2 :
        return False
    
    if no == 2:
        return True
    
    for i in range(2,no):
        if no%i==0:
            return False
    
    return True