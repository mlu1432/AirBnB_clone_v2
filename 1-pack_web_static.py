#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive from the contents
of the web_static folder.
"""

from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    All archives must be stored in the folder versions.
    The name of the archive created must be
    web_static_<year><month><day><hour><minute><second>.tgz.
    Returns the archive path if the archive has been correctly generated.
    Otherwise, returns None.
    """
    try:
        # Create the versions directory if it doesn't exist
        if not os.path.exists("versions"):
            os.makedirs("versions")

        # Create the archive name with the current date and time
        now = datetime.now()
        archive_name = "versions/web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))

        # Create the archive
        local("tar -cvzf {} web_static".format(archive_name))

        return archive_name
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
