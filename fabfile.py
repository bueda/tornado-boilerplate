#!/usr/bin/env python
"""Fabfile using only commands from buedafab (https://github.com/bueda/ops) to
deploy this app to remote servers.
"""

import os
from fabric.api import *

from buedafab.test import test, django_test_runner as _django_test_runner, lint
from buedafab.deploy.types import django_deploy as deploy
from buedafab.environments import (django_development as development,
        django_production as production, django_localhost as localhost,
        django_staging as staging)
from buedafab.tasks import (setup, restart_webserver, rollback, enable,
        disable, maintenancemode, rechef)

# For a description of these attributes, see https://github.com/bueda/ops

env.unit = "boilerplate"
env.path = "/var/django/%(unit)s" % env
env.scm = "git@github.com:bueda/%(unit)s.git" % env
env.scm_http_url = "http://github.com/bueda/%(unit)s" % env
env.wsgi = "wsgi/%(unit)s.wsgi" % env
env.root_dir = os.path.abspath(os.path.dirname(__file__))

env.pip_requirements = ["requirements/common.txt",
        "vendor/allo/pip-requirements.txt",]
env.pip_requirements_dev = ["requirements/dev.txt",]
env.pip_requirements_production = ["requirements/production.txt",]
