#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive from the web_static folder.
"""
import os
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Compresses the contents of the web_static folder into a .tgz archive.
    Returns:
        - Archive path if successful, None otherwise.
    """
    # Create the "versions" directory if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Get the current date and time
    dt = datetime.now()

    # Define the filename with the current timestamp
    filename = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)

    # Use the tar command to create the .tgz archive
    result = local("tar -cvzf {} web_static".format(filename))

    # Check if the archive was created successfully
    if result.succeeded:
        return filename
    else:
        return None
