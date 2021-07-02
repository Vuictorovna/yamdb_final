from rest_framework import permissions


class IsAdminRole(permissions.BasePermission):
    def has_permission(self, request, view):

        return request.user.is_authenticated and request.user.is_user_admin


class IsAdminRoleOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_user_admin
        )


class ReviewCommentPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
            or request.user.is_user_admin
            or request.user.is_user_moderator
        )
