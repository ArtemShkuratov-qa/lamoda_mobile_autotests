import lamoda_mobile_autotests
from pathlib import Path

def abs_path_from_project(relative_path: str):
    return (
        Path(lamoda_mobile_autotests.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )