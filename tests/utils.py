from pathlib import Path

HERE = Path(__file__).parent.resolve()


def load_data(path: str) -> list[str]:
    target = (HERE / Path(path)).resolve()
    with open(target) as f:
        return f.readlines()
