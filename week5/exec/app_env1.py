"""
Print all environment variables defined on your system. The output will be the
same as running `env` command on unix like systems or `set` on a Windows command
prompt.
"""

import os


def main():
    for key, val in os.environ.items():
        print(f"{key}={val}")


if __name__ == "__main__":
    main()
