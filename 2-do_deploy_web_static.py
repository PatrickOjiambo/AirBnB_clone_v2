#!/usr/bin/python3
"""
Distributes an archive to my web servers
"""


from fabric.api import env, run, put
import os
env.hosts = ["100.26.246.25", "100.25.23.198"]


def do_deploy(archive_path):
    """
    distributes an archive to my web servers
    """
    if os.path.exists(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, '/tmp/{}'.format(file)).failed() is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzvf /tmp/{} -C /data/web_static/releases/{}".format(file, name)).failed() is True:
        return False
    if run("rm /tmp/{}".format(file)).failed() is True:
        return False
    if run("rm -rf /data/web_static/current").failed() is True:
        return False
    if run("ln -sf /data/web_static/releases/{} /data/web_static/current".format(name)).failed() is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    return True
