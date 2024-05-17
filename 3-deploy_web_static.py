#!/usr/bin/python3
"""
Fabric script to create and distribute an archive to web servers.
"""

from fabric.api import env, local, put, run
from datetime import datetime
import os

env.hosts = ['100.26.156.194', '3.94.213.104']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    All archives must be stored in the folder versions
    (this folder should be created if it doesn’t exist).
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

def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.
    Args:
        archive_path (str): The path to the archive to be deployed.
    Returns:
        bool: True if all operations were successful, False otherwise.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Extract archive filename and name without extension
        filename = os.path.basename(archive_path)
        no_ext = os.path.splitext(filename)[0]
        release_path = "/data/web_static/releases/{}".format(no_ext)

        # Upload the archive to the /tmp/ directory on the server
        put(archive_path, "/tmp/")

        # Create the release directory
        run("mkdir -p {}".format(release_path))

        # Uncompress the archive to the release directory
        run("tar -xzf /tmp/{} -C {}".format(filename, release_path))

        # Delete the archive from the server
        run("rm /tmp/{}".format(filename))

        # Move files to the proper directory
        run("mv {}/web_static/* {}/".format(release_path, release_path))

        # Delete the extraneous directory
        run("rm -rf {}/web_static".format(release_path))

        # Delete the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_path))

        return True
    except Exception as e:
        print(f"Deployment failed: {e}")
        return False

def deploy():
    """
    Packs and deploys the web_static content.
    Returns:
        bool: True if all operations were successful, False otherwise.
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
