#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
import os
import re


env.hosts = ['34.227.91.56', '52.3.249.59']
env.user = "ubuntu"


def do_pack():
    """
    Function that generates a .tgz archive from the contents of the web_static
    """

    local("mkdir -p versions")
    now = datetime.utcnow()
    archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
        now.year, now.month, now.day, now.hour, now.minute, now.second)
    result = local("tar -cvzf versions/{} web_static".format(archive_name))

    if result.succeeded:
        return os.path.join("versions", archive_name)
    else:
        return None


def do_deploy(archive_path):
    """ This function destributes an archive to my web servers
    """
    if not os.path.exists(archive_path):
        return False

    file_name = re.search(r"([^\/]*)\..*$", archive_path)[1]
    releases_path = f"/data/web_static/releases/{file_name}"

    put(archive_path, "/tmp/")
    run("sudo mkdir -p {}".format(releases_path))
    run("sudo tar -zxf /tmp/{}.tgz -C {}".format(file_name, releases_path))
    run("sudo cp -rf {}/web_static/* {}".format(releases_path, releases_path))
    run("sudo rm -r {}/web_static".format(releases_path))
    run("sudo rm -rf /data/web_static/current")
    run("sudo ln -s {} /data/web_static/current".format(releases_path))
    print("New version deployed!")
    return True


def deploy():
    """ This function calls do_pack and do_deploy
    """
    archive_path = do_pack()
    if not archive_path:
        return False

    return do_deploy(archive_path)
