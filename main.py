# Define a function to calculate factorial recursively
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Main function to interact with the user
def main():
    # Input
    num = int(input("Enter a non-negative integer: "))

    # Processing
    result = factorial(num)

    # Output
    print(f"The factorial of {num} is {result}")

# Entry point of the program
if __name__ == "__main__":
    main()
2