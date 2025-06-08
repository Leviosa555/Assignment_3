import math

try:
    number = float(input("Enter a number: "))

    sqrt_val = math.sqrt(number)
    log_val = math.log(number)
    sine_val = math.sin(number)

    print(f"Square root: {sqrt_val}")
    print(f"Logarithm: {log_val}")
    print(f"Sine: {sine_val}")

except ValueError:
    print("Invalid input! Please enter a valid number.")
except Exception as e:
    print(f"Error: {e}")
