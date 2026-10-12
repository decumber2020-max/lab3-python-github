"""python_calc.py - A feature-rich command-line calculator."""
 
 
def add(a, b):
    return a + b
 
 
def subtract(a, b):
    return a - b
 
 
def multiply(a, b):
    return a * b
 
 
def divide(a, b):
    if b == 0:
        return None  # signals division by zero
    return a / b
 
 
def check_even_odd(n):
    if n != int(n):
        return "not a whole number, so it is neither even nor odd"
    return "even" if int(n) % 2 == 0 else "odd"
 
 
def percentage(part, whole):
    if whole == 0:
        return None  # cannot take a percentage of zero
    return (part / whole) * 100

 
 
def show_menu():
    print("\n===== Python Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Check Even/Odd")
    print("6. Calculate Percentage")
    print("7. Exit")
 
 
def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()#strip removes spaces from input
 
        if choice == "7":
            print("Goodbye!")
            break
 
        if choice not in {"1", "2", "3", "4", "5", "6"}:
            print("Invalid choice. Please enter a number from 1 to 7.")
            continue
 
        if choice == "5":
            n = float(input("enter a number:"))
            print(f"Result: {n} is {check_even_odd(n)}.")
 
        elif choice == "6":
            part = int(input("Enter the first number (part): "))
            whole = int(input("Enter the second number (whole): "))
            result = percentage(part, whole)
            if result is None:
                print("Error: cannot calculate a percentage of zero.")
            else:
                print(f"Result: {part} is {result}% of {whole}.")
 
        else:
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
 
            if choice == "1":
                print(f"Result: {a} + {b} = {add(a, b)}")
            elif choice == "2":
                print(f"Result: {a} - {b} = {subtract(a, b)}")
            elif choice == "3":
                print(f"Result: {a} × {b} = {multiply(a, b)}")
            elif choice == "4":
                result = divide(a, b)
                if result is None:
                    print("Error: division by zero is not allowed.")
                else:
                    print(f"Result: {a} ÷ {b} = {result}")
 
 
main()

