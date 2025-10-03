"""
How to handle input from environment variables.

From your shell try running this program once to see what it prints out. Next,
from your shell type the following:

`export CONFIG_VAR=something` (Mac/Linux zsh/sh/bash etc.)
`set CONFIG_VAR=something` (Windows cmd.exe)

Then run it again.
"""

import os


def main():
    value = os.environ.get("CONFIG_VAR")
    if value is not None:
        print(f"Configured value set to {value}")
    else:
        print("Config var not set")


if __name__ == "__main__":
    main()
