from ping_log_parser.parser import parse

import pytest

from tests.utils import load_data


@pytest.mark.parametrize(
    ("data", "expected"),
    [
        (
            load_data("./assets/test1.txt"),
            ["Server 192.168.2.198 is dead since 2021-11-28 22:47:05 to 2021-11-28 22:47:06"],
        ),
        (
            load_data("./assets/test2.txt"),
            [
                "Server 192.168.43.252 is dead since 2021-11-28 23:12:07 to 2021-11-28 23:12:07",
                "Server 10.254.216.249 is dead since 2021-11-28 23:12:01 to 2021-11-28 23:12:01",
            ],
        ),
        (load_data("./assets/test3.txt"), []),
    ],
)
def test_q1_parse(data, expected):
    result = parse(data)
    assert result == expected
