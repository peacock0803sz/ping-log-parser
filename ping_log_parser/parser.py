from __future__ import annotations
from argparse import ArgumentParser
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Literal

HERE = Path(__file__).parent.resolve()


@dataclass
class Record:
    """ログの1レコードを表現する"""

    timestamp: datetime
    address: str
    response: int | Literal["-"]


def parse(src: list[str]) -> list:  # type: ignore
    """文字列のリストを受け取り、サーバーがタイムアウトしていた期間を返却する"""
    result = []
    previous = Record(timestamp=datetime.now(), address="127.0.0.1", response=1)
    for line in src:
        split_line = line.split(",")
        if len(split_line) != 3:
            continue

        dt = datetime.strptime(split_line[0], "%Y%m%d%H%M%S")
        addr = split_line[1]
        res = int(split_line[2].strip()) if split_line[2].strip() != "-" else "-"
        record = Record(timestamp=dt, address=addr, response=res)

        if previous.response == "-":
            msg = f"Server {previous.address} is dead since {previous.timestamp} to {record.timestamp}"  # noqa
            result.append(msg)
        previous = record
    return result


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
