#!/usr/bin/python3
"""
Fabric script to delete out-of-date archives.
"""

from fabric.api import env, local, run
import os

env.hosts = ['100.26.156.194', '3.94.213.104']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'

def do_clean(number=0):
    """
    Deletes out-of-date archives.
    Args:
        number (int): The number of archives to keep.
                      If number is 0 or 1, keep only the most recent version of your archive.
                      If number is 2, keep the most recent, and second most recent versions of your archive.
                      etc.
    """
    number = int(number)
    if number < 1:
        number = 1

    # Local cleanup
    archives = sorted(os.listdir("versions"))
    archives = [archive for archive in archives if archive.endswith(".tgz")]
    [archives.pop() for _ in range(number)]
    for archive in archives:
        local("rm -f versions/{}".format(archive))

    # Remote cleanup
    run("ls -t /data/web_static/releases | grep web_static | awk 'NR>{}'".format(number))
    run("ls -t /data/web_static/releases | grep web_static | awk 'NR>{}' | xargs -I {} rm -rf /data/web_static/releases/{}".format(number))
