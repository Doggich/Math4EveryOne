import argparse
import sys


def fibonacci(n: int) -> int:
    """
    Calculates the nth Fibonacci number.

    :param n: The position of the Fibonacci number to calculate.
    :return: The nth Fibonacci number.
    """
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


def main():
    parser = argparse.ArgumentParser(description="Calculate the nth Fibonacci number.")
    parser.add_argument("n", type=int, help="The position of the Fibonacci number to calculate.")
    parser.add_argument("-h", "--help", action="help", help="Show this help message and exit.")

    args = parser.parse_args()

    try:
        result = fibonacci(abs(args.n))
        print(f"The {args.n}th Fibonacci number is: {result}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
