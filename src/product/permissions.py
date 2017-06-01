from rest_framework import permissions


class AdminWriteOnly(permissions.IsAuthenticated):
    """
    Global permission check for user blogs.
    """

    def has_permission(self, request, view):
        if request.user and (request.user.is_staff or request.user.is_superuser):
            return True
        if request.method.lower() in ["post", "patch", "put", "delete"]:
            return False
        return True
