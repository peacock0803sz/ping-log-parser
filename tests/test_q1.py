from ping_log_parser.parser import parse

import pytest

from tests.utils import load_data


@pytest.mark.parametrize(
    ("data", "expected"),
    [
        (
            load_data("./assets/test1.txt"),
            [
                "Server 192.168.10.14/28 is dead since 2021-11-29 00:45:03 to 2021-11-29 00:45:03",
                "Server 192.168.10.12/28 is dead since 2021-11-29 00:45:06 to 2021-11-29 00:45:06",
            ],
        ),
        (
            load_data("./assets/test2.txt"),
            ["Server 10.0.10.121/24 is dead since 2021-11-29 00:46:06 to 2021-11-29 00:46:06"],
        ),
        (
            load_data("./assets/test3.txt"),
            [
                "Server 10.0.100.196/24 is dead since 2021-11-29 00:48:04 to 2021-11-29 00:48:05",
                "Server 10.0.100.34/24 is dead since 2021-11-29 00:48:06 to 2021-11-29 00:48:06",
                "Server 10.0.100.15/24 is dead since 2021-11-29 00:48:04 to 2021-11-29 00:48:04",
            ],
        ),
    ],
)
def test_q1_parse(data, expected):
    result = parse(data)
    assert result == expected
