#!/usr/bin/python3
"""
A fabric script that generates a .tgz archive
"""
from fabric.api import local
from datetime import datetime

"""
A function to generate .tgz archive
"""
def do_pack():
    """
    Create a date variable as well as a file path variable for the location
    of your archive.
    The date variable will serve as the date which the file was archived
    """
    date = datetime.utcnow().strftime("%y%m%d%H%M%S")
    file_path = "versions/web_static_{}.tgz".format(date)

    """
    Create a directory /versions in your current folder.
    We will run this in the local machine using the local function to
    run commands in the local machine. Secondly we will create archive
    using the same local function
    """
    local("mkdir -p ./versions")
    create_path = local("sudo -cvz --file={} ./web_static".format(file_path))
    if create_path is not None:
        return file_path
    else:
        return None

