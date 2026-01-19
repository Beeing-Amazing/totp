""" """

import os


CONFIG_DIR: os.PathLike = os.path.expanduser("~/.config/totp/")
HASH_FILE: os.PathLike = os.path.join(CONFIG_DIR, "data.json")
SITES_TABLE: os.PathLike = os.path.join(CONFIG_DIR, "totp.db")

LOG_DIR: os.PathLike = os.path.expanduser("~/.local/share/totp/logs/")
LOG_LEVEL: str = "INFO"

BLANK_DEF: str = " "
NICK_DEF: str = "#"
SLIDER_DEF: list[str] = ["█", "◣", " "]
SITE_DEF: str = "https://www.github.com/"
DEFAULT_FG: str = "white"
FANCY_SLIDER: bool = False

ENTRY_SCHEMA: dict = {
    "line1": [
        {"type": "site", "width": 20, "alignment": "left"},
        {"type": "token", "alignment": "right", "space_before": 8},
    ],
    "line2": [
        {"type": "nick", "width": 32, "alignment": "left", "space_after": 8},
        {"type": "token_time", "precision": 1, "alignment": "right"},
    ],
    "border": [
        {"type": "filler", "filler": " "}
    ]
}

STATUSLINE_SCHEMA: dict = {
    "border": [
        {"type": "filler", "filler": "-"}
    ],
    "line1": [
        {"type": "time", "format": "%H:%M:%S", "alignment": "left"},
        {"type": "slider", "width": 16, "alignment": "right"}
    ],
}
