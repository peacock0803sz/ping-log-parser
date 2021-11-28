from ping_log_parser.parser import calc_timeout

import pytest

from tests.utils import load_data


@pytest.mark.parametrize(
    ("data", "expected", "retry"),
    [
        (
            load_data("./assets/test1.txt"),
            [
                "Server 192.168.10.14/28 is dead since 2021-11-29 00:45:03 to 2021-11-29 00:45:03",
                "Server 192.168.10.12/28 is dead since 2021-11-29 00:45:06 to 2021-11-29 00:45:06",
            ],
            0,
        ),
        (load_data("./assets/test2.txt"), [], 3),
        (load_data("./assets/test3.txt"), [], 10),
    ],
)
def test_q2_parse(data, expected, retry):
    result = calc_timeout(data, retry)
    assert result == expected
