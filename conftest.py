import pathlib
from dataclasses import dataclass

import pytest

UI_TESTS_ROOT = pathlib.Path().resolve()


@pytest.fixture(scope="session")
def settings():
    return Settings(UI_TESTS_ROOT)


@dataclass
class Settings:
    ui_tests_root: pathlib.Path
