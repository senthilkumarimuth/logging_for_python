import toml
import os
from pathlib import Path, PurePath

file_path=PurePath(Path(__file__).parents[0]).as_posix()
config = toml.load(os.path.join(file_path, "config.toml"))
