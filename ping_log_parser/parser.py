from __future__ import annotations
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from operator import attrgetter
from typing import Literal


@dataclass()
class Record:
    """ログの1レコードを表現する"""

    timestamp: datetime
    address: str
    response: int | Literal["-"]


def _parse(src: list[str]) -> list[Record]:
    records = []
    for line in src:
        split_line = line.split(",")
        if len(split_line) != 3:
            continue

        dt = datetime.strptime(split_line[0], "%Y%m%d%H%M%S")
        addr = split_line[1]
        res: int | Literal["-"] = (
            int(split_line[2].strip()) if split_line[2].strip() != "-" else "-"
        )
        records.append(Record(timestamp=dt, address=addr, response=res))
    return records


def calc_timeout(src: list[str], retry: int = 0) -> list[str]:
    """文字列のリストを受け取り、サーバーがタイムアウトしていた期間を返却する"""
    result = []
    count = 0
    previous = Record(timestamp=datetime.now(), address="127.0.0.1", response=1)
    for record in _parse(src):
        if previous.response == "-":
            count += 1
            if count > retry:
                msg = f"Server {previous.address} is dead since {previous.timestamp} to {record.timestamp}"  # noqa
                result.append(msg)
        previous = record
    return result


def calc_load(src: list[str], time: int, threshold: int) -> list[str]:
    records = _parse(src)
    _sorted_ip = sorted(records, key=attrgetter("address"))
    sorted_ip_ts = sorted(_sorted_ip, key=attrgetter("timestamp"))

    high_loads = defaultdict(list)
    for r in sorted_ip_ts:
        if r.response == "-":
            high_loads[r.address].append(threshold)
        elif r.response > threshold:
            high_loads[r.address].append(r.response)

    result = []
    for addr, load_times in high_loads.items():
        average = sum(load_times[: time - 1]) / time
        result.append(f"Server {addr} was high load time {average}")

    return result
