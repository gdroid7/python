def displayNumInReverse(num):
    for i in range(num,0,-1):
        print(i)

def main():
    displayNumInReverse(int(input("Enter number : ")))
    return

if __name__ == "__main__":
    main()