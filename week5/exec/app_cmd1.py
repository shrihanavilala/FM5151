"""
Display arguments passed into a program.

Try the following examples:

- python cmd1.py
- python cmd1.py arg1 arg2
- python cmd1.py --opt1=True
"""

import sys


def main():
    # sys.argv captures program followed by arguments in a list
    print(sys.argv)


if __name__ == "__main__":
    main()
