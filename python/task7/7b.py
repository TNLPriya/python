def add(a, b):
        return a + b
def subtract(a, b):
    return a - b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b if b != 0 else "Error: Division by zero"

# Regular function for greeting
greet = lambda name: f"Hello, {name}! Welcome to the program."

def main():
    # Demonstrating the use of lambda functions
    num1 = int(input("enter num1:"))
    num2 = int(input("enter num2:"))
    
    print("Arithmetic Operations:")
    print("Sum of", num1, "and", num2, ":", add(num1, num2))
    diff=subtract(num1, num2)
    print("Difference between", num1, "and", num2, ":", diff)
    if diff< 0:
        print("The difference is negative!")
    elif diff==0:
        print("The difference is Zero!")
    else:
        print("The difference is Positive!")

    print("Product of", num1, "and", num2, ":", multiply(num1, num2))
    print("Quotient of", num1, "and", num2, ":", divide(num1, num2))    
    # Greeting the user
    user_name = "Alice"
    print("\nGreeting:")
    print(greet(user_name))

# Run the main function
if __name__ == "__main__":
    main()
