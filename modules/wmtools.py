#!/usr/bin/python
# -*- coding: latin-1 -*-

import os, sys, inspect
from io import StringIO, BytesIO
from hashlib import sha1
from datetime import datetime
import pandas as pd
import textwrap

try :
    import pywikibot as pb
    from pywikibot.specialbots import UploadRobot
except :
    current_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
    folder_parts = current_folder.split(os.sep)
    pywikibot_folder = os.sep.join(folder_parts[:-2])

    if current_folder not in sys.path:
        sys.path.insert(0, current_folder)
    if pywikibot_folder not in sys.path:
        sys.path.insert(0, pywikibot_folder)

    import pywikibot as pb
    from pywikibot.specialbots import UploadRobot

commons_site = pb.Site("commons", "commons")

def is_commons_file (sha):
    pages = pb.site.APISite.allimages(commons_site, sha1=sha)
    result = False
    for page in pages :
        print (page)
        result = True
        break
    return result
    
def get_hash (file_path):
    image_file = open(file_path, "rb")
    byte_stream = BytesIO(image_file.read()).getvalue()
    image_file.close()
    hashObject = sha1()
    hashObject.update(byte_stream)
    return hashObject.hexdigest()