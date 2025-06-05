
def printPattern(col):
    if col <= 0 :
        return
    
    for i in range(col):
        str="\n"
        for j in range(col,i,-1):
            str+="\t * \t"
        print(str)

def main():
    printPattern(int(input("Enter no : ")))
    return

if __name__ == "__main__":
    main()