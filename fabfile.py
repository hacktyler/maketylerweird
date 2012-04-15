#!/usr/bin/env

from fabric.api import *

def reload():
    local('vagrant ssh -c "localwiki-manage collectstatic --noinput"')
    local('vagrant ssh -c "sudo service apache2 restart"')

