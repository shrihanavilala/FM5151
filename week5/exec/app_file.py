import json
from datetime import datetime


def main():
    with open("cfg.json") as f:
        cfg = json.load(f)

    print(cfg["a_config_string"])
    print(cfg["some_list"])
    print(datetime.fromisoformat(cfg["a_timestamp"]))


if __name__ == "__main__":
    main()
