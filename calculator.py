

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        return None


def main():
    num1_str = input("Enter first number: ")
    num2_str = input("Enter second number: ")
    op = input("Enter operation:(+,/,-,*))")

    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
    except ValueError:
        print("You shud enter valid numbers")
        exit()

    if op == "+":
        result = add(num1, num2)
    elif op == "-":
        result = subtract(num1, num2)
    elif op == "*":
        result = multiply(num1, num2)
    elif op == "/":
        result = divide(num1, num2)
    else:
        print("Invalid operation")
        exit()

    if result is None:
        print("Error becoz cant divide with Zero")
        exit()

    print(f"The result is {result}")


if __name__ == "__main__":
    main()
