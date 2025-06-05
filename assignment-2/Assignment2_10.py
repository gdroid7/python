def noOfDigits(str):
    sum=0
    for i in range(len((str))):
        sum+=int(str[i])
    return sum

def main():
    print("Addition of digits : ",noOfDigits(input("Enter string : ")))
    return

if __name__ == '__main__':
    main()