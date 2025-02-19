from subprocess import run as run_command
from builder import build_project

def upload_to_pypi(pkg: str = "fouri"):
    if isinstance(pkg, str):
        build_project()
        
        print("checking twine...")
        run_command(["python3", "-m", "pip", "install", "--upgrade", "twine"], check=True)
        
        print(f"{pkg} is uploading to pypi")
        run_command(["python3", "-m", "twine", "upload", "dist/*"], check=True)