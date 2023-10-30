def main():
    y = float(input("Enter the angle in degrees (0 <= y <= 360): "))

    return f"Number of full hours: {int(y/30)} hours and number of full minutes: {int(y / 0.5)} minutes"

if __name__ == "__main__":
    print(main())