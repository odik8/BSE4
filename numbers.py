def main():
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    n3 = int(input("Enter third number: "))
    n4 = int(input("Enter fourth number: "))

    return round((n1 + n2) / (n3 + n4), 2)


if __name__ == "__main__":
    print(main())
