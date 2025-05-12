from subprocess import run as run_command
from builder import build_project


def run_project(pkg: str = "fouri"):
    build_project()

    # install project
    print("installing locale pakcages...")
    run_command(["python3", "-m", "pip", "install", "--upgrade", "."], check=True)

    run_command(["python3", "-m", pkg])
    pass
