def checkPrime(no):
    
    if no < 2 :
        return "invalid no"
    
    if no == 2:
        return "a prime number"
    
    for i in range(2,no):
        if no%i==0:
            return "not a prime number"
    
    return "a prime number"

def main():
    print("The number is : ",checkPrime(int(input("Enter no : "))))
    return

if __name__ == "__main__":
    main()