from rest_framework import permissions


class CustomPermission(permissions.IsAuthenticated):
    message = 'Adding customers not allowed.'

    def has_object_permission(self, request, view, obj):
        print(view, obj.__dict__)
        if not obj.user == request.user.id:
            return False
        return True
