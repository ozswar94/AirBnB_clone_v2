#!/usr/bin/python3
""" function pack files for transfer more light"""
from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """ archive file """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        filename = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(filename))
        return filename
    except Error:
        return None
