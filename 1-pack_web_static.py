#!/usr/bin/python3
from fabric import *
from datetime import datetime
import os
'''
fabric script that generates a .tgz archive from the contents of the web_static
'''


def do_pack():
    """ funct that do generat .tgz and list the return"""

    local("mkdir -p versions")
    now = datetime.utcnow
    archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
        now.year, now.month, now.day, now.hour, now.minute, now.second)
    result = local("tar -cvzf versions/{} web_static".format(archive_name))
    if result.failed:
        return None
    else:
        return os.path.join("versions", archive_name)
