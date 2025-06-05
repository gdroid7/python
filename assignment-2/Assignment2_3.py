def factorial(no):
    result=no
    for i in range(no-1,1,-1):
        result*=i
    return result

def main():
    print("Factorial is : ",factorial(int(input("Enter no : "))))
    
if __name__ == "__main__":
    main()