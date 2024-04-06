import random
import string

from .models import URLmodel

SHORT_LEN = 6

def get_short():
    short = ''.join(random.choices(string.ascii_letters + string.ascii_letters, k=SHORT_LEN))
    if URLmodel.query.filter(URLmodel.short == short).first():
        return get_short()
    else:
        return short