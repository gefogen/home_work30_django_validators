from rest_framework import permissions


class IsCreatedBy(permissions.BasePermission):
    message = 'Только пользователь, создавший обьявление, может удалить его.'

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False