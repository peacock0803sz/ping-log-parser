from argparse import ArgumentParser
from datetime import datetime
from ipaddress import ip_network
from pathlib import Path
import random

HERE = Path(__file__).parent.resolve()


def gen_dummy(size: int) -> list[str]:
    now = datetime.now()
    data = []
    res = "0"
    addr = "127.0.0.1"
    for i in range(size):
        dt = now.strftime("%Y%m%d%H%M" + str(i).zfill(2)[-2])
        parent = random.choice(["192.168.0.0", f"10.{random.randint(1, 255)}.0.0"])
        addr = random.choice(list(ip_network(f"{parent}/16"))) if res != "-" else addr
        res_time = random.randint(0, 500)
        res = str(res_time) if res_time else "-"
        data.append(f"{dt},{addr},{res}\n")
    return data


def main():
    parser = ArgumentParser()
    parser.add_argument("size", type=int)
    parser.add_argument("--dest", "-d", type=Path)
    args = parser.parse_args()

    if args.size < 10:
        exit(1)
    data = gen_dummy(args.size)
    dest = HERE / args.dest.resolve().resolve()
    with open(dest, "w") as f:
        f.writelines(data)


if __name__ == "__main__":
    main()
