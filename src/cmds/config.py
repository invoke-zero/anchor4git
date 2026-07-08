from pathlib import Path

from ..consts import *
from ..utils import *


def config_cmd() -> None:
    """Open the defaut text editor app with the project config open."""

    # ───── SAFETY GATEWAY ────────────────────────────────────────────────── #
    git_existance_safety()
    repo_existance_safety()

    open_editor(Path(CONFIG_FILE))