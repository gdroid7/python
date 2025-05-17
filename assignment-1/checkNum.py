def numType(num):
    if num == 0:
        return "zero"
    elif num > 0:
        return "positive"
    else:
        return "negative"

def main():
    print("Number is :",numType(int(input("Enter number : "))))

if __name__ == "__main__":
    main()