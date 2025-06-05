def factors(no):
    factors=[]
    result=no+1
    for i in range(no-1,1,-1):
        if no%i==0:
            result+=i
            factors.append(i)
    return result,factors

def main():
    a,b=factors(int(input("Enter a number : ")))
    print("Factors are : ",b)
    print("Addition of factors is : ",a)
    
if __name__ == "__main__":
    main()
    