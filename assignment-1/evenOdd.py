def checkNum(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
def main():
    print(checkNum(int(input("Enter a number: "))))
    return

if __name__ == "__main__":
    main()