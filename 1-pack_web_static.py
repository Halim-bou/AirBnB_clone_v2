#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Function that generates a .tgz archive from the contents of the web_static"""

    local("mkdir -p versions")
    now = datetime.utcnow()
    archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
        now.year, now.month, now.day, now.hour, now.minute, now.second)
    result = local("tar -cvzf versions/{} web_static".format(archive_name))

    if result.succeeded:
        return os.path.join("versions", archive_name)
    else:
        return None
