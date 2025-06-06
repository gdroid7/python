def checkPrime(no):
    
    if no < 2 :
        return False
    
    if no == 2:
        return True
    
    for i in range(2,no):
        if no%i==0:
            return False
    
    return True

def main():
    if checkPrime(int(input("Enter no : "))):
        print("The number is : prime")
    else:
        print("The number is : not prime")
    return

if __name__ == "__main__":
    main()