import pathlib

def get_seed_filepath(name):
    definitions_dir = pathlib.Path(__file__).parent
    f = definitions_dir / "seeds" / name
    return f.as_posix()