import os
import site
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
if os.path.splitext(os.path.basename(__file__))[0] == 'cProfile':
    if os.environ.get('DJANGO_APP_PATH'):
        ROOT = os.environ['DJANGO_APP_PATH']
    else:
        print 'When using cProfile you must set $DJANGO_APP_PATH'
        sys.exit(2)

path = lambda *a: os.path.join(ROOT, *a)

prev_sys_path = list(sys.path)

site.addsitedir(path('apps'))
site.addsitedir(path('lib'))
if os.path.exists(path('vendor')):
    for directory in os.listdir(path('vendor')):
        full_path = path('vendor/%s' % directory)
        if os.path.isdir(full_path):
            site.addsitedir(full_path)

# Move the new items to the front of sys.path. (via virtualenv)
new_sys_path = []
for item in list(sys.path):
    if item not in prev_sys_path:
        new_sys_path.append(item)
        sys.path.remove(item)
sys.path[:0] = new_sys_path

os.environ['CELERY_LOADER'] = "django"
