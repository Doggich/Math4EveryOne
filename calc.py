import sys
from math import pi, e, log


def get_number(arg):
    """Converts the argument to a number, handling 'pi' and 'e' as special cases."""
    if arg == "pi":
        return pi
    elif arg == "e":
        return e
    else:
        try:
            return float(arg)
        except ValueError:
            raise ValueError(f"Invalid input: {arg} is not a valid number.")


def perform_operation(operation, num1, num2):
    """Performs the specified arithmetic operation."""
    if operation == 'add':
        return num1 + num2
    elif operation == 'sub':
        return num1 - num2
    elif operation == 'mul':
        return num1 * num2
    elif operation == 'div':
        if num2 == 0:
            raise ZeroDivisionError("Division by zero!")
        return num1 / num2
    elif operation == 'pow':
        return num1 ** num2
    elif operation == 'mod':
        if num2 == 0:
            raise ZeroDivisionError("Modulus by zero!")
        return num1 % num2
    elif operation == 'div_int':  # Integer division
        if num2 == 0:
            raise ZeroDivisionError("Integer division by zero!")
        return num1 // num2
    elif operation == "log":
        if num2 <= 0 or num1 <= 0:
            raise ValueError("Logarithm base and argument must be positive.")
        return log(num1, num2)
    else:
        raise ValueError(f"Invalid operation: {operation}")


def main():
    if len(sys.argv) != 4:
        print(f"Usage: python {sys.argv} <operation> <number1> <number2>")
        sys.exit(1)

    try:
        operation = sys.argv[1].lower()
        num1 = get_number(sys.argv[2])
        num2 = get_number(sys.argv[3])
        result = perform_operation(operation, num1, num2)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
