#!/usr/bin/env

from fabric.api import *

def reload():
    local('vagrant ssh -c "localwiki-manage collectstatic --noinput"')

