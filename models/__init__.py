#!/usr/bin/python3
"""
Create an unique FileStorage
"""

import os
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

if os.getenv("HBNB_TYPE_STORAGE") == 'db':
    storage = FileStorage()
else:
    storage = FileStorage()
storage.reload()
