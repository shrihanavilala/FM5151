"""
Using the `argparse` library provided as a part of the standard library.

Try the following examples:

- python app_cmd2.py
- python app_cmd2.py -h
- python app_cmd2.py "Hi there"
- python app_cmd2.py "Hi there" --times=5
- python app_cmd2.py "Hi there" --print-green
- python app_cmd2.py "Hi there" --times=5 --print-green
- python app_cmd2.py "Hi there" --print-green --times=3
"""

from argparse import ArgumentParser, Namespace


def parse_arguments() -> Namespace:
    """Grabs the arguments passed in from the command-line and validates them"""
    parser = ArgumentParser(prog="Example Application")
    parser.add_argument("print_value", type=str, help="Value to print")
    parser.add_argument("--times", type=int, help="How many times", default=1)
    parser.add_argument(
        "--print-green", help="Whether to print as green", action="store_true"
    )
    return parser.parse_args()


def main(args: Namespace):
    print(f"Arguments provided: {args}")

    value = args.print_value
    if args.print_green:
        value = "\033[92m" + value + "\033[0m"

    for _ in range(args.times):
        print(value)


if __name__ == "__main__":
    args = parse_arguments()
    main(args)
