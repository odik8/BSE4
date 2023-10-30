def main():
    distance = float(input("Enter the distance between cars in kilometers: "))
    speed1 = float(input("Enter the speed of the first car in km/h: "))
    speed2 = float(input("ВEnter the speed of the second car in km/h: "))

    return f"The cars will meet in, {distance / (speed1 + speed2)}, hours"

if __name__ == "__main__":
    print(main())