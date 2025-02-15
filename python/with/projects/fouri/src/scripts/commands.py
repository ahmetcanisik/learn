from builder import build_project
from upload import upload_to_pypi
from install import install_project
from run import run_project
from reinstall import reinstall_project

command_list = [
    {
        "name": "build",
        "run": build_project
    },
    {
        "name": "upload",
        "run": upload_to_pypi
    },
    {
        "name": "reinstall",
        "run": reinstall_project
    },
    {
        "name": "run",
        "flags": [
            {
                "flag": "--install",
                "run": install_project
            }
        ],
        "run": run_project
    }
]