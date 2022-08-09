import os
import sys
import site

site.addsitedir('/var/www/arabic/env/lib/python/site-packages')
sys.path.append('/var/www/arabic/')

# We defer to a DJANGO_SETTINGS_MODULE already in the environment. This breaks
# if running multiple sites in the same mod_wsgi process. To fix this, use
# mod_wsgi daemon mode with each site in its own daemon process, or use
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "arabic.settings")


activate_env=os.path.expanduser("/var/www/arabic/env/bin/activate_this.py")
#execfile(activate_env, dict(__file__=activate_env))
exec(compile(open(activate_env, "rb").read(), activate_env, 'exec'))

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()