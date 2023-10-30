def main():
    name = input("What is your name?: ")
    age = input("How old are you?: ")
    area = input("Where are you live?: ")

    return f"This is {name} \nIt is {age} \n(S)he lives in {area}"


if __name__ == "__main__":
    print(main())
