def sub_two_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 - num2
        print(f"The difference of {num1} and {num2} is {result}")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    sub_two_numbers()
