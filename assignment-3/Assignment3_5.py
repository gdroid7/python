import MarevellousNum

def ListPrime(list):
    sum=0
    for i in list:
        if MarevellousNum.checkPrime(i):
            sum+=i
    return sum

def acceptInput(n):
    list=[]
    for i in range(n):
        list.append(int(input("Enter no : ")))
    return list

def main():
    print("Addition of all prime no is : ",ListPrime(acceptInput(int(input("Input number of elements: ")))))
    return

if __name__ == "__main__":
    main()