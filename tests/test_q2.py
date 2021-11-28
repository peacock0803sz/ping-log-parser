from ping_log_parser.parser import parse

import pytest

from tests.utils import load_data


@pytest.mark.parametrize(
    ("data", "expected", "retry"),
    [
        (
            load_data("./assets/test1.txt"),
            ["Server 192.168.2.198 is dead since 2021-11-28 22:47:05 to 2021-11-28 22:47:06"],
            0,
        ),
        (
            load_data("./assets/test2.txt"),
            [],
            3
        ),
        (load_data("./assets/test3.txt"), [], 2),
    ],
)
def test_q2_parse(data, expected, retry):
    result = parse(data, retry)
    assert result == expected
