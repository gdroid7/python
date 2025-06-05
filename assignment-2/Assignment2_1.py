from arithmatic import add,sub,div,mult

def calc(a,b):
    print("addition        = ",add(a,b))
    print("subtraction     = ",sub(a,b))
    print("multiplication  = ",mult(a,b))
    print("division        = ",div(a,b))
    return

def main():
    calc(int(input("Enter first number : ")),int(input("Enter second number : ")))
    return

if __name__ == "__main__":
    main()