def frequency(list,searchElem):
    freq=0
    for i in list:
        if i == searchElem:
            freq+=1
    return freq

def acceptInput(n):
    list=[]
    for i in range(n):
        list.append(int(input("Enter no : ")))
        
    searchElem=int(input("Element to search : "))
    return list,searchElem

def main():
    list,search=acceptInput(int(input("Input number of elements: ")))
    print("Frequency of the no is : ",frequency(list,search))
    return

if __name__ == "__main__":
    main()