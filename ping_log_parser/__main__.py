from argparse import ArgumentParser
from pathlib import Path

from ping_log_parser.parser import calc_load, calc_timeout

HERE = Path(__file__).parent.resolve()


def main():
    parser = ArgumentParser()
    parser.add_argument("src", type=Path, help="Path to log file")
    parser.add_argument("--retry", "-r", type=int, help="Retry times", default=0)
    parser.add_argument(
        "--time", "-N", type=int, help="Times to calculate average response (0=disable)", default=0
    )
    parser.add_argument(
        "--threshold", "-t", type=int, help="Threshold of average response time (ms)", default=900
    )
    args = parser.parse_args()

    src = HERE / args.src.resolve()
    with open(src, "r") as f:
        data = f.readlines()
        timeouts = calc_timeout(data, args.retry)
        for s in timeouts:
            print(s)
        if args.time < 1 and args.threshold < 1:
            high_loads = calc_load(data, args.time, args.threshold)
            for s in high_loads:
                print(s)


if __name__ == "__main__":
    main()
