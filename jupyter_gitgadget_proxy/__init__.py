import os
import logging

from typing import Any
from typing import Dict


logger = logging.getLogger(__name__)
logger.setLevel("INFO")


def setup_gitgadget() -> Dict[str, Any]:
    """Setup commands and icon paths and return a dictionary compatible
    with jupyter-server-proxy.
    """

    def _get_icon_path():
        return os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "icons", "gitgadget.svg"
        )

    return {
        "command": [
            "/usr/local/bin/R",
            "-e",
            f"options(gitgadget.jupyter=TRUE); gitgadget::gitgadget(host='0.0.0.0', port={port}, launch.browser=FALSE)",
        ],
        "timeout": 30,
        "new_browser_tab": True,
        "launcher_entry": {"title": "GitGadget", "icon_path": _get_icon_path()},
    }
