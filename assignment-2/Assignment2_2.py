def printStarryPattern(no):
    for i in range(no):
        row="\n"
        for j in range(no):
            row+="\t * \t"
        print(row)
    return

def main():
    printStarryPattern(int(input("Enter no of stars : ")))
    
if __name__ == "__main__":
    main()