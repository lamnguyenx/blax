#!/usr/bin/env python3

# Copyright 2024 (author: lamnguyenx)


# commons
import os
from pathlib import Path
from platformdirs import user_cache_dir
from _black_version import version as __version__



### FUNCTIONS
def get_cache_dir__BLAX() -> Path:
    default_cache_dir = user_cache_dir('blax.black')
    cache_dir = Path(os.environ.get('BLAX_BLACK_CACHE_DIR', default_cache_dir))
    cache_dir = cache_dir / __version__
    return cache_dir
