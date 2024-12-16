import sys
from random import randint, uniform

# Define modes for integer and float
int_mode = ["-i", "int", "-int"]
float_mode = ["-f", "float", "-float"]


def get_usage_message():
    """Returns the usage message for the script."""
    return f"Usage: python {sys.argv} <mode> <min_value> <max_value>\n" \
           f"Modes: {', '.join(int_mode)} for integers, {', '.join(float_mode)} for floats"


def main():
    if len(sys.argv) != 4:
        print(get_usage_message())
        sys.exit(1)

    try:
        mode = sys.argv[1].lower()
        if mode in int_mode:
            min_num, max_num = int(sys.argv[2]), int(sys.argv[3])
            if min_num > max_num:
                min_num, max_num = max_num, min_num
            print(randint(min_num, max_num))
        elif mode in float_mode:
            min_num, max_num = float(sys.argv[2]), float(sys.argv[3])
            if min_num > max_num:
                min_num, max_num = max_num, min_num
            print(uniform(min_num, max_num))
        else:
            print("Incorrect mode. Use one of the following modes:")
            print(f"Integers: {', '.join(int_mode)}")
            print(f"Floats: {', '.join(float_mode)}")
            sys.exit(1)
    except ValueError:
        print("Error: Invalid type of values. Please enter valid numbers.")
        print(get_usage_message())
        sys.exit(1)


if __name__ == "__main__":
    main()
