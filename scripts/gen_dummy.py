from argparse import ArgumentParser
from datetime import datetime
from ipaddress import ip_network
from pathlib import Path
import random

HERE = Path(__file__).parent.resolve()


def gen_dummy(size: int, base: int, prefix=16) -> list[str]:
    now = datetime.now()
    data = []
    res = "0"
    addr = "127.0.0.1"
    for i in range(size):
        dt = now.strftime("%Y%m%d%H%M" + str(i).zfill(2)[-2])
        addr = random.choice(list(ip_network(f"{base}/{prefix}"))) if res != "-" else addr
        res_time = random.randint(0, 500)
        res = str(res_time) if res_time else "-"
        data.append(f"{dt},{addr}/{prefix},{res}\n")
    return data


def main():
    parser = ArgumentParser()
    parser.add_argument("dest", type=Path)
    parser.add_argument("size", type=int)
    parser.add_argument("--base", "-b", type=str, default="192.168.0.0")
    parser.add_argument("--prefix", "-p", type=int)
    args = parser.parse_args()

    if args.size < 10:
        exit(1)
    data = gen_dummy(args.size, args.base, args.prefix)
    dest = HERE / args.dest.resolve().resolve()
    with open(dest, "w") as f:
        f.writelines(data)


if __name__ == "__main__":
    main()
