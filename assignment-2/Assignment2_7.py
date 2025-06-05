
def printPattern(col):
    if col <= 0 :
        return
    
    for i in range(1,col+1):
        str="\n"
        for j in range(1,col+1):
            str+=f"\t {j} \t"
        print(str)

def main():
    printPattern(int(input("Enter no : ")))
    return

if __name__ == "__main__":
    main()