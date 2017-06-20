from rest_framework import permissions


class CustomPermission(permissions.IsAuthenticated):
    message = 'Adding customers not allowed.'

    def has_object_permission(self, request, view, obj):
        print(obj.user, request.user.id)
        if not obj.user == request.user.id:
            print("sadasdsad")
            return False
        return True
