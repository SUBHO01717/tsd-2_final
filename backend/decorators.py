from django.core.exceptions import PermissionDenied
from accounts.models import *
from backend.models import *
from django.shortcuts import redirect
# def role_required(allowed_roles=[]):
#     def decorator(func):
#         def wrap(request, *args, **kwargs):
#             try:
#                 user_role = request.user.userprofile.userrole
#                 if user_role in allowed_roles:
#                     return func(request, *args, **kwargs)
#                 else:
#                     raise PermissionDenied
#             except UserProfile.DoesNotExist:
#                 raise PermissionDenied
#         return wrap
#     return decorator


def role_required(allowed_roles=[]):
    def decorator(func):
        def wrap(request, *args, **kwargs):
            try:
                user_role = request.user.userprofile.userrole
                if user_role in allowed_roles:
                    return func(request, *args, **kwargs)
                else:
                    # Redirect to a page indicating permission denied
                    return redirect('permission_denied')  # Replace 'permission_denied' with the name of your HTML page
            except UserProfile.DoesNotExist:
                # Redirect to a page indicating permission denied
                return redirect('permission_denied')  # Replace 'permission_denied' with the name of your HTML page
        return wrap
    return decorator