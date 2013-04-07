#!/usr/bin/env

from fabric.api import *

# Environments
def dev():
    env.hosts = ['vagrant@127.0.0.1:2222']
    env.key_filename = '~/.vagrant.d/insecure_private_key'

def prod():
    env.hosts = ['ubuntu@maketylerweird.com:22']

# Deployment 
def reload():
    sudo('localwiki-manage collectstatic --noinput')

def deploy():
    put('themes', '/usr/share/localwiki', use_sudo=True)
    sudo('localwiki-manage collectstatic --noinput')
    sudo('service apache2 restart')

# Backups
def backup_db(filename):
    sudo('pg_dump -U postgres localwiki > /tmp/.localwiki_backup.sql', user='postgres')

    get('/tmp/.localwiki_backup.sql', filename)
    sudo('rm /tmp/.localwiki_backup.sql')

def restore_db(filename):
    put(filename, '/tmp/.localwiki_backup.sql')

    sudo('psql -c "DROP DATABASE localwiki"', user='postgres')
    sudo('createdb -T template_postgis localwiki', user='postgres')
    sudo('psql localwiki < /tmp/.localwiki_backup.sql', user='postgres')

    run('rm /tmp/.localwiki_backup.sql')
