from .help import *
from .version import *


def get_commands():
    return [
        {
            "name": "version",
            "flags": ["version", "-v", "-version", "--version"],
            "fn": get_version,
        },
        {"name": "help", "flags": ["help", "-h", "-help", "--help"], "fn": need_help},
    ]
