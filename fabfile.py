#!/usr/bin/env

from fabric.api import *

def reload():
    local('vagrant ssh -c "sudo localwiki-manage collectstatic --noinput"')

