#!/usr/bin/python3
""" pack and deploy archive"""
from datetime import datetime
from fabric.api import env, put, local, run
from os.path import isdir, exists
env.hosts = ['34.139.53.21', '35.196.110.215']


def do_pack():
    """ archive file """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        filename = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(filename))
        return filename
    except Exception:
        return None


def do_deploy(archive_path):
    """ deploy archive on server """
    if exists(archive_path) is False:
        return False
    try:
        filename = archive_path.split('/')[-1]
        fname_noext = filename.split('.')[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, fname_noext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(filename, path, fname_noext))
        run('rm /tmp/{}'.format(filename))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, fname_noext))
        run('rm -rf {}{}/web_static'.format(path, fname_noext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, fname_noext))
        print("New version deployed!")
        return True
    except Exception as e:
        print(e)
        return False


def deploy():
    """ deploy script """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
