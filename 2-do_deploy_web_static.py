#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers.
"""

from fabric.api import env, put, run
import os

env.hosts = ['100.26.156.194', '3.94.213.104']  # Replace with your server IPs
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'  # Path to your SSH private key

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
