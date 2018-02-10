import os
import sys
import docker
import sqlite3
from datetime import date, datetime
import time


def get_dir_size(path):
    total = 0
    for entry in os.scandir(path):
        try:
            is_dir = entry.is_dir(follow_symlinks=False)
        except OSError as error:
            print('Error calling is_dir():', error, file=sys.stderr)
            continue
        if is_dir:
            total += get_dir_size(entry.path)
        else:
            try:
                total += entry.stat(follow_symlinks=False).st_size
            except OSError as error:
                print('Error calling stat():', error, file=sys.stderr)
    return total


def publish_data():
    conn = sqlite3.connect('volumes.db')
    c = conn.cursor()
    client = docker.from_env()
    volume = client.volumes.list()
    time = datetime.now()
    for volumes in volume:
        name = volumes.name
        mountpoint = volumes.attrs['Mountpoint']
        size = get_dir_size(mountpoint)
        c.execute("INSERT INTO volumes VALUES (?,?,?,?)", (time, name, mountpoint, size))
    conn.commit()
    conn.close()


if __name__ == '__main__':
    publish_data()
    time.sleep(3600)
