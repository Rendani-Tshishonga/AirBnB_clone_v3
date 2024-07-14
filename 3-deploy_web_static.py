#!/usr/bin/python3
"""
A Bash script that distributes an archive to your web servers
using the deploy module.
"""
import os
from frabric.api import *
from datetime import datetime


env.hosts = ['34.239.250.29', '54.160.126.116']

"""
A function to generate .tgz archive
"""
def do_pack():
    date = datetime.utcnow().strftime("%y%m%d%H%M%S")
    file_path = "versions/web_static_{}.tgz".format(date)

    try:
        local("mkdir -p ./versions")
        local("tar -cvz --file={} ./web_static".format(file_path))
    except:
        return None


def do_deploy(archive_path):
    """
    Test whether the archive file is present
    if  not return false
    """
    if os.path.isfile(archive_path) is False:
        return False
    """
    Try to execute commands on our ebsite to transfer file
    """
    try:
        archive = archive_path.split("/")[-1]
        path = "/data/web_static/releases"
        put("{}".format(archive_path), '/tmp/{}'.format(archive))
        new_dir = archive.split('.')
        run("mkdir -p {}/{}/".format(path, new_dir[0]))
        archive_new = ".".join(new_dir)
        run("tar -xzf /tmp/{} -C {}/{}/".format(archive_new, path, new_dir[0]))
        run("rm /tmp/{}".format(archive_new))
        run("mv {}/{}/web_static/* {}/{}/".format(path, new_dir[0], path, new_dir[0]))
        run("rm -rf {}/{}/web_static".format(path, new_dir[0]))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/{}/ /data/web_static/current".format(path, new_dir[0]))
        return True
    except:
        return False

def deploy():
    """
    store the archived path in a variable
    created_path
    """
    created_path = do_pack()
    if created_path is None:
        return false
    else:
        return do_deploy(created_path)
