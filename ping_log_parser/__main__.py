from argparse import ArgumentParser
from pathlib import Path

from ping_log_parser.parser import parse

HERE = Path(__file__).parent.resolve()


def main():
    parser = ArgumentParser()
    parser.add_argument("--src", "-s", type=Path, help="Path to log file")
    args = parser.parse_args()

    src = HERE / args.src.resolve()
    with open(src, "r") as f:
        result = parse(f.readlines())
        for s in result:
            print(s)


if __name__ == "__main__":
    main()
