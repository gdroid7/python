def maxOf(list):
    max=0
    for i in list:
        if max < i:
            max=i
    return max

def acceptInput(n):
    list=[]
    for i in range(n):
        list.append(int(input("Enter no : ")))
    return list

def main():
    print("Max no is : ",maxOf(acceptInput(int(input("Input number of elements: ")))))
    return

if __name__ == "__main__":
    main()