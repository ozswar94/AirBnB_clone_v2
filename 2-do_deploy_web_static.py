#!/usr/bin/python3
""" definition of do_depliy function """
from fabric.api import put, run, env
from os.path import exists
env.hosts = ['34.139.53.21', '35.196.110.215']


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
        return True
    except Exception:
        return False
