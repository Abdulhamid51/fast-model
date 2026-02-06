from .models import *
from fast_model.import_libs import *
from functools import wraps
from django.core.exceptions import PermissionDenied

def user_type_required(allowed_types=[]):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                if hasattr(request.user, 'custom') and request.user.custom.user_type in allowed_types:
                    return view_func(request, *args, **kwargs)
            raise PermissionDenied
        return _wrapped_view
    return decorator
