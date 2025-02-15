from importlib.metadata import version

def get_version(pkg_name: str = "fouri") -> str:
    try:
        v = version(pkg_name)
        if v:
            return v
        
        raise NameError("version not found!")
    except NameError as e:
        print(str(e))