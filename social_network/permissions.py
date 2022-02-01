from rest_framework import permissions


class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve', 'update', 'partial_update', 'destroy']:
            return request.user.is_authenticated
        elif view.action == 'create':
            return True