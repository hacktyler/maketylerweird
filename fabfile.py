#!/usr/bin/env

from fabric.api import *

env.user = 'ubuntu'
env.hosts = ['maketylerweird.com']

def reload():
    local('vagrant ssh -c "sudo localwiki-manage collectstatic --noinput"')

def deploy():
    put('themes', '/usr/share/localwiki', use_sudo=True)
    sudo('localwiki-manage collectstatic --noinput')
    sudo('service apache2 restart')

