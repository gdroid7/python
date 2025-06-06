def add(listOfNumbers):
    sum=0
    for i in listOfNumbers:
        sum+=i
    return sum

def acceptInput(n):
    list=[]
    for i in range(n):
        list.append(int(input("Enter no : ")))
    return list

def main():
    print("Addition is : ",add(acceptInput(int(input("Input number of elements: ")))))
    return

if __name__ == "__main__":
    main()