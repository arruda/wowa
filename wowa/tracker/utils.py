# -*- coding: utf-8 -*-
import json

from django.utils.functional import Promise
from django.utils.encoding import force_text


class JSONLazyEncoder(json.JSONEncoder):
    """Encodes django's lazy i18n strings.
    Used to serialize translated strings to JSON, because
    simplejson chokes on it otherwise.
    """
    def default(self, obj):
        if isinstance(obj, Promise):
            return force_text(obj)
        return obj
