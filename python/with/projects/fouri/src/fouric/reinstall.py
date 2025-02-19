from install import install_project
from uninstall import uninstall_project

def reinstall_project():
    uninstall_project()
    install_project()