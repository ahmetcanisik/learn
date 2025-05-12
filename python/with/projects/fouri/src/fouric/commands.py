from reinstall import reinstall_project
from install import install_project
from run import run_project
from upload import upload_to_pypi
from builder import build_project
from uninstall import uninstall_project

"""
How to use?

[
    {
        # {str} Command Name
        "name": "Upload To PYPI v2.0.4",

        # {str | list[str]} Command executed name and alias flags. and more.
        "args": ["upload", "u", "-u", "--upload"],
        
        # {str} printing text on the screen.
        "print": "uploading your project to pypi..."
        
        # {void referance} execute function.
        "execute": my_func_referance
    }
]
"""
command_list = [
    {"name": "Version", "args": ["version", "-v", "--version"], "print": "0.0.1"},
    {
        "name": "Help",
        "args": ["help", "-h", "--help"],
        "print": "usage: python3 -m fouric [command]",
    },
    {"name": "Build", "args": "build", "execute": build_project},
    {"name": "Upload", "args": "upload", "execute": upload_to_pypi},
    {"name": "Uninstall", "args": "uninstall", "execute": uninstall_project},
    {"name": "ReInstall", "args": "reinstall", "execute": reinstall_project},
    {
        "name": "Run",
        "args": "run",
        "options": [{"option": "--install", "run": install_project}],
        "execute": run_project,
    },
]
