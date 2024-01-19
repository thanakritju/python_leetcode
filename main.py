import sys

import utils


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 main.py generate <id>")
        return

    try:
        command = sys.argv[1]
        arg = sys.argv[2]

        if command == "generate":
            print(f"The problem name of {arg} is {utils.get_name_by_id(int(arg))}")
        else:
            print("Invalid command")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")


if __name__ == "__main__":
    main()
