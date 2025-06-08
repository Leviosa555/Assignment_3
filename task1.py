def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

try:
    number = int(input("Enter a number: "))
    result = factorial(number)

    if result is not None:
        print(f"Factorial of {number} is: {result}")
    else:
        print("Factorial is not defined for negative numbers.")
except ValueError:
    print("Invalid input! Please enter an integer.")
