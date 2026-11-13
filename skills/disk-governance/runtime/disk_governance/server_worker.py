"""Subprocess entry used only for the locally spawned service."""
import sys
from pathlib import Path
from .server import _serve
from .database import DataPaths

_serve(DataPaths(Path(sys.argv[1])),int(sys.argv[2]))

