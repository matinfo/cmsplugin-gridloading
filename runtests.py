import sys
import os

import django


cmd = 'coverage run `which djangocms-helper` cmsplugin_gridloading test --cms --extra-settings=test/settings'

if django.VERSION[:2] < (1, 6):
    cmd += ' --runner=discover_runner.DiscoverRunner'

sys.exit(os.system(cmd))
