"""
Lavalink connecter
~~~~~~~~~~~~~~~
:copyright: (c) 2021-2026 HazemMeqdad
:copyright (c) 2021-2026 vladpochuev (modifications):
:license: MIT, see LICENSE for more details.
"""

__title__ = "lavaplay.py"
__author__ = "vladpochuev"
__license__ = "MIT"
__version__ = "1.0.20.3"

from .client import Lavalink
from .objects import *
from .events import *
from .rest import RestApi
from .exceptions import (
    NodeError, FiltersError, VolumeError,
    NotConnectedError, ConnectedError, TrackLoadFailed
)
from .node_manager import Node
