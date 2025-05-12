from subprocess import run as run_command


def install_project(pkg: str = "fouri"):
    print(f"installing {pkg}...")
    run_command(["python3", "-m", "pip", "install", "--upgrade", pkg], check=True)
