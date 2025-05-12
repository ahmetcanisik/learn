from subprocess import run as run_command
from uninstall import uninstall_project

"""
Builder

- pip uninstall package_name
- rm -rf dist build
- python3 -m build
- 
"""


def build_project(pkg: str = "fouri"):
    if isinstance(pkg, str):
        print(f"uninstalling {pkg}...")
        uninstall_project()

        print("removing to old build files...")
        run_command(["rm", "-rf", "dist"], check=True)

        print("building project...")
        run_command(["python3", "-m", "build"], check=True)
