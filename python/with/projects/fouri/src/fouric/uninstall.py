from subprocess import run as run_command


def uninstall_project(pkg: str = "fouri"):
    print(f"uninstalling... {pkg}")
    run_command(["python3", "-m", "pip", "uninstall", pkg, "-y"], check=True)
