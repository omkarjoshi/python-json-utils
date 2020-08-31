

def _readfile(path: str = None):
    if path is None:
        raise FileNotFoundError
    return open(path)