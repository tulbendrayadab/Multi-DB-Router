from Systango_proj.settings.base import *

DEBUG = False

try:
    from Systango_proj.settings.local import *
except:
    pass