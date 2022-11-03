from rest_framework import permissions

from users.models import User


class IsCreatedByOrAdminOrModerator(permissions.BasePermission):
    message = 'Только пользователь, создавший объявление, amdin и модераторы может изменять или удалять его.'

    def has_object_permission(self, request, view, obj):
        if request.user.role == User.ADMIN or request.user.role == User.MODERATOR:
            return True
        if obj.author == request.user:
            return True
        return False